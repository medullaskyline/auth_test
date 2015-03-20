import sys
import os


sys.path.append(os.path.join(os.getcwd(), "lib", "django.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "userena.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "django-guardian.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "easy-thumbnails.zip"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'auth_test.settings'