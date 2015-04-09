import sys
import os

sys.path.append(os.path.join(os.getcwd(), "lib", "allauth.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "apiclient.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "django.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "httplib2.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "googleapiclient.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "openid.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "oauth2client.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "pyasn1.zip"))  # for GOOGLE_APPLICATION_CREDENTIALS
sys.path.append(os.path.join(os.getcwd(), "lib", "pyasn1_modules.zip"))  # for GOOGLE_APPLICATION_CREDENTIALS
sys.path.append(os.path.join(os.getcwd(), "lib", "requests.zip"))  # replaced v2.6 with v2.3 for django-allauth
sys.path.append(os.path.join(os.getcwd(), "lib", "requests_oauthlib.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "rsa.zip"))  # for GOOGLE_APPLICATION_CREDENTIALS
sys.path.append(os.path.join(os.getcwd(), "lib", "six.zip"))
sys.path.append(os.path.join(os.getcwd(), "lib", "uritemplate.zip"))


os.environ['DJANGO_SETTINGS_MODULE'] = 'auth_test.settings'