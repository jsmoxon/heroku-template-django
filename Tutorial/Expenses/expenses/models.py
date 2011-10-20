import datetime
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, unique=True)

    def get_absolute_url(self):
        """
        Needed for the profiles application, returns a url ref
        """
        return 'profiles_profile_detail', (), { 'username': self.user.username }
	get_absolute_url = models.permalink(get_absolute_url)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()
    class Meta:
        verbose_name_plural = "people"


class Household(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    persons = models.ManyToManyField(Person)

    def __unicode__(self):
        return '%s: %s' % (self.name, ', '.join(str(person) for person in self.persons.all()))

    def balance(self):
        """
        returns a list of household members, with an additional field, balance,
        added to all members
        balance - the amount above debt for the household member on all household transactions
        """
        persons = self.persons.all()
        table = dict((person.id, dict(up=0., down=0.)) for person in persons)
        for transaction in self.transaction_set.all():
            up_down = transaction.up_down_table()
            for k,v in up_down.iteritems():
                table[k]['up']+=v['up']
                table[k]['down']+=v['down']
        out_persons = []
        for k,v in table.iteritems():
            person = self.persons.get(id=k)
            person.balance = v['down'] - v['up']
            out_persons.append(person)
        return out_persons

            

            


        

class Transaction(models.Model):
    household = models.ForeignKey(Household)
    transactor = models.ForeignKey(Person)
    creation_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    cost = models.FloatField()
    tax = models.FloatField(default=0.0)

    def total_cost(self):
        """
        total cost of transaction
        """
        return self.cost*(self.tax + 1.)


    def up_down_table(self):
        """
        table with transaction member ID as key
        values are a dictionary
        up: the amount a member is up on the transaction
        down: same
        These values are aggregated over all transactions by Household to produce the balance value
        """
        total_cost = self.total_cost()
        persons = self.household.persons.all()
        table = dict((person.id, dict(up=0., down=0.)) for person in persons)
        table[self.transactor_id]['down']+=total_cost
        for multiplier in self.multiplier_set.all():
            table[multiplier.person_id]['up']+=multiplier.multiplier*total_cost
        return table


    def tax_percent(self):
        """
        pretty printing
        """
        return '%.1f %%' % round(self.tax*100, 2)

    def cost_dollar(self):
        """
        pretty printing
        """
        return '$%.2f' % round(self.cost, 3)


    def save(self, *args, **kwargs):
        """
        if item already exists, and just modifying, then super, and return
        if not
        create a multiplier for each transaction member, where default is clean split of all costs
        """
        if self.id:
            super(Transaction, self).save(*args, **kwargs)
            return
        super(Transaction, self).save(*args, **kwargs)
        nMembers = self.household.persons.count()
        def_multipliers = 1./nMembers
        for person in self.household.persons.all():
            Multiplier(person= person, multiplier = def_multipliers, transaction = self).save()

    def __unicode__(self):
        return 'trans: %s, household: %i' % (self.transactor, self.household_id)

class Multiplier(models.Model):
    person = models.ForeignKey(Person)
    multiplier = models.FloatField()
    transaction = models.ForeignKey(Transaction)

    def multiplier_percent(self):
        """
        for printing
        """
        return '%.1f %%' % round(self.multiplier*100, 2)

    def __unicode__(self):
        return '%f - %s' % (self.multiplier, self.person)

    class Meta:
        """
        unique on a person and transaction
        """
        unique_together = (('person', 'transaction'),)
