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
    'django.contrib.staticfiles'
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

CLOUD_BASE_URL = "https://isb-cgc.appspot.com"
LOCAL_BASE_URL = "http://localhost:8080"

##########################
# For django-userena_app #
##########################

INSTALLED_APPS += (
    'userena_app',
    'guardian',
    'easy_thumbnails',
    'userena'
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# EMAIL_BACKEND = 'django.core.mail.console.EmailBackend'  # backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testymctest02@gmail.com'
EMAIL_HOST_PASSWORD = 'MyNewPass'

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'userena_app.MyProfile'

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

USERENA_SIGNIN_REDIRECT_URL = '/userena_app/%(username)s/'
LOGIN_URL = '/userena_app/signin/'
LOGOUT_URL = '/userena_app/signout/'
LOGIN_REDIRECT_URL = '/userena_app/profile/'



USERENA_SIGNIN_AFTER_SIGNUP = True

MIDDLEWARE_CLASSES += ('userena.middleware.UserenaLocaleMiddleware',)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )


##########################
# End django-userena_app #
##########################





ROOT_URLCONF = 'auth_test.urls'

WSGI_APPLICATION = 'auth_test.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
