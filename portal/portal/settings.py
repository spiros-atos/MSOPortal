"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.contrib.messages import constants as message_constants
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = config('DEBUG')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
INTERNAL_IPS = (
    '127.0.0.1', 'localhost'
)

# Application definition

INSTALLED_APPS = [
    'sso.apps.SsoConfig',
    'experimentstool.apps.ExperimentstoolConfig',
    'remotedesktops.apps.RemotedesktopsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',

    'portal.middleware.RedirectOnCancelMiddleware'
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'portal/templates'),
                 os.path.join(BASE_DIR, 'sso/templates'),
                 os.path.join(BASE_DIR, 'experimentstool/templates'),
                 os.path.join(BASE_DIR, 'remotedesktops/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                "portal.context_processors.custom_vars",
            ],
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'sso.backends.keyrock.KeyrockOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join('sso', 'static'),
    os.path.join('experimentstool', 'static'),
    os.path.join('remotedesktops', 'static')
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# X_FRAME_OPTIONS = 'ALLOW-FROM ' + config('FIWARE_IDM_ENDPOINT')
# X_FRAME_OPTIONS = 'DENY'

MARKETPLACE_URL = config('MARKETPLACE_URL')
DATACATALOGUE_URL = config('DATACATALOGUE_URL')

ORCHESTRATOR_HOST = config('ORCHESTRATOR_HOST')
ORCHESTRATOR_USER = config('ORCHESTRATOR_USER')
ORCHESTRATOR_PASS = config('ORCHESTRATOR_PASS')
ORCHESTRATOR_TENANT = config('ORCHESTRATOR_TENANT')

FIWARE_IDM_ENDPOINT = config('FIWARE_IDM_ENDPOINT')
SOCIAL_AUTH_FIWARE_KEY = config('SOCIAL_AUTH_FIWARE_KEY')
SOCIAL_AUTH_FIWARE_SECRET = config('SOCIAL_AUTH_FIWARE_SECRET')

# MESSAGE_LEVEL = message_constants.DEBUG
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login_error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
