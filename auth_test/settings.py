"""
Django settings for auth_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y74l@53h8s%c=7%72z1%*4t+5o-n+@jvb-!n@yko&$om7_%=(x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bq_app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CLOUD_BASE_URL = "https://test-authentic.appspot.com"
LOCAL_BASE_URL = "http://localhost:8080"

ROOT_URLCONF = 'auth_test.urls'

WSGI_APPLICATION = 'auth_test.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth',)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

# ANONYMOUS_USER_ID = -1

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/test-authentic:auth-test-cloudsql-instance',
            'NAME': 'userena_db',
            'USER': 'root'
        }
    }
    API_BASE = CLOUD_BASE_URL
    SITE_ID = 4  # test-authentic.appspot.com

elif os.getenv('SETTINGS_MODE') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '173.194.249.186',
            'NAME': 'userena_db',
            'USER': 'root',
            'PASSWORD': 'password'
        }
    }
    API_BASE = LOCAL_BASE_URL
    SITE_ID = 3  # localhost:8080

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'userena_db',
            'USER': 'root',
            'PASSWORD': 'password'
        }
    }
    API_BASE = LOCAL_BASE_URL
    SITE_ID = 3  # localhost:8080


##########################
#  Start django-allauth  #
##########################

LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS += (
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google')

TEMPLATE_CONTEXT_PROCESSORS += (
    'allauth.socialaccount.context_processors.socialaccount',
    'allauth.account.context_processors.account',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS += (
    os.path.join(BASE_DIR, 'templates', 'accounts'),
    )

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' }
        }
    }


##########################
#   End django-allauth   #
##########################

