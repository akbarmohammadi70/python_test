from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fxbrbb!tw71gkpsp@3jds5agy-bz4!k#y-ewn^8e%=jd#7s4%#'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#INSTALLED_APPS = []

SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'qazwsx',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
    
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
