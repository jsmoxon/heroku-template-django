from django_bootstrap import bootstrap
bootstrap(__file__ + '/../')
from django.contrib.sites.models import Site
from constants import *
from django.contrib.auth.models import User


site = Site.objects.get_current()
site.domain = DOMAIN
site.name = DOMAIN_NAME
site.save()
User.objects.create_superuser(ADMIN_UN, ADMIN_UE, ADMIN_PW).save()

