"""
Django settings for registration project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')^#aguz07!_p^tya%n6uc4ncc*$q2iao_q2(pa+0(!2-l-(b%v'

# SECURITY WARNING: don't run with debug turned on in production!
def env_var(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

DEBUG = env_var('DEBUG', True)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'regApp',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'registration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'registration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# I N T E R N A T I O N A L I Z A T I O N  BEGIN
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'ka-ge'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
gettext = lambda s: s
LANGUAGES = (
    ('ka', gettext('Georgian')),
)
# I N T E R N A T I O N A L I Z A T I O N  END


# S T A T I C   F I L E S   BEGIN
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = env_var('ABS_PATH_BASE', '') + 'media/'
STATIC_URL = '/static/'
STATIC_ROOT = env_var('ABS_PATH_BASE', '') + 'static_gather/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    #os.path.join(BASE_DIR, 'media'),
    os.path.join(BASE_DIR, 'FndRegister/css'),    
)
# S T A T I C   F I L E S   END

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 2

#MAIL SETTINGS
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'npc_mailbox'
EMAIL_HOST_PASSWORD = 'BlackViking13'
EMAIL_PORT = 587