from django.contrib.auth.models import Permission, ContentType

content_type_id = ContentType.get(name='my profile')
Permission.objects.create(name='Can change profile', content_type_id=content_type_id, codename='change_profile')
Permission.objects.create(name='Can delete profile', content_type_id=content_type_id, codename='delete_profile')