import os
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

MEDIA_ROOT = BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

BOT_SECRET_KEY = env('BOT_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

# Aplicactions and it's entry command
BOT_APPS = [
    'tcrb.apps.places',
    'tcrb.apps.transportation',
    'tcrb.apps.services',
    'tcrb.apps.tutorias',
    'tcrb.apps.news',
    'tcrb.apps.directory',
    'tcrb.apps.pages',
    'tcrb.apps.search',
    'tcrb.apps.tracking',
    'tcrb',
]

PAGINATION_LIMIT = 5

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + BOT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

LOGGING = {
    'version': 1,
    # The version number of our log
    'disable_existing_loggers': False,

    'handlers': {
        'info': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': BASE_DIR / 'debug.log'
        },
    },
    # A logger for WARNING which has a handler called 'file'. A logger can have multiple handler
    'loggers': {
        # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            # notice how file variable is called in handler which has been defined above
            'handlers': ['info', 'debug'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s | %(module)s] %(message)s",
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-CR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
