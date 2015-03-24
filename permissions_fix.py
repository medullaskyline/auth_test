# from auth_test import settings
# DJANGO_SETTINGS_MODULE = settings

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'auth_test.settings')
import django
django.setup()
from django.contrib.auth.models import Permission, ContentType

content_type = ContentType.objects.get(name='my profile')
content_type_id = int(content_type.id)
if not Permission.objects.filter(name='Can change profile', content_type_id=content_type_id, codename='change_profile'):
    p1 = Permission.objects.create(name='Can change profile', content_type_id=content_type_id, codename='change_profile')
    p1.save()
if not Permission.objects.filter(name='Can delete profile', content_type_id=content_type_id, codename='delete_profile'):
    p2 = Permission.objects.create(name='Can delete profile', content_type_id=content_type_id, codename='delete_profile')
    p2.save()