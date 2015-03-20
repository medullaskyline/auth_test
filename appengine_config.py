import sys
import os


sys.path.append(os.path.join(os.getcwd(), "lib", "django.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "easy_thumbnails.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "guardian.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "html2text.py.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "six.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "userena.zip"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'auth_test.settings'