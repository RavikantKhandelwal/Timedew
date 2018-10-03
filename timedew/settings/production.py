import os
from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECRET_KEY = '^5l0(_fya95g@(0g=e6eu*y%g21c4@yk)#m=#v4an4idxp9t(='
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [".elasticbeanstalk.com", ".timedew.com", ".timesdew.com"]
if 'RDS_DB_NAME' in os.environ:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.environ['RDS_DB_NAME'],
			'USER': os.environ['RDS_USERNAME'],
			'PASSWORD': os.environ['RDS_PASSWORD'],
			'HOST': os.environ['RDS_HOSTNAME'],
			'PORT': os.environ['RDS_PORT'],

		}
	}
else:
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

# for s3
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
		'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
		'Cache-Control': 'max-age=94608000',
	}


AWS_STORAGE_BUCKET_NAME = 'timedew-static'
AWS_ACCESS_KEY_ID = 'AKIAIBL3EDI3U7RC244Q'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATICFILES_LOCATION = 'static'

STATICFILES_STORAGE = 'timedew.settings.custom_storages.StaticStorage'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'timedew.settings.custom_storages.MediaStorage'


SITE_ID = 2  # for that add site timedew to the Sites model in timedew
