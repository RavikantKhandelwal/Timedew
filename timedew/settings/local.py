from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^5l0(_fya95g@(0g=e6eu*y%g21c4@yk)#m=#v4an4idxp9t(='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.103']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timedew',
        'USER': 'timedewuser',
        'PASSWORD': '1234abcd',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

SITE_ID = 2

# Either enable sending mail messages to the console:
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

