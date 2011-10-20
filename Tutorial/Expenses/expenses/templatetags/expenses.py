__author__ = 'jackdreilly'

from django import template
register = template.Library()


@register.inclusion_tag('expenses/household.html')
def render_household(household):
    """
    render html for a household
    in turn calls the render_person method for members
    """
    return dict(household = household)

@register.inclusion_tag('expenses/household_preview.html')
def render_household_pv(household):
    """
    render html for a household preview
    in turn calls the render_person method for members
    """
    return dict(household = household)



@register.inclusion_tag('expenses/person.html')
def render_person(person):
    """
    render html for a single person
    """
    return dict(person = person)

@register.filter
def percentage(decimal):
    return format(decimal, "%")

@register.inclusion_tag('expenses/transaction_create_tag.html')
def render_transaction_create(household):
    return dict(household=household)

@register.inclusion_tag('expenses/household_transaction_create_tag.html')
def render_household_transaction_create(household):
    return dict(household=household)

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)