from django.contrib.admin import site
from models import *

site.register(Person)
site.register(Household)
site.register(Multiplier)
site.register(Transaction)


