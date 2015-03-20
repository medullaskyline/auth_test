from django.contrib.sites.models import Site

#

Site.objects.create(pk=2, domain='localhost:8000', name='localhost:8000')
Site.objects.create(pk=3, domain='localhost:8080', name='localhost:8080')
Site.objects.create(pk=4, domain='test-authentic.appspot.com', name='test-authentic.appspot.com')