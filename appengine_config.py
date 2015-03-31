import sys
import os

sys.path.append(os.path.join(os.getcwd(), "lib", "allauth.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "django.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "easy_thumbnails.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "guardian.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "html2text.py.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "openid.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "requests.zip")) # replaced v2.6 with v2.3
sys.path.append(os.path.join(os.getcwd(), "lib", "requests_oauthlib.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "six.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "userena.zip"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'auth_test.settings'