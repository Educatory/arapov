import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_PROJECT_NAME = 'project_name'
DEBUG = False
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)n_t!ir_xc218#$rewr8tk$%yt#f6do=0zi9+p($@r)*)$yjg('

# Application definition

INSTALLED_APPS = [

    # django default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'django_extensions',
    'django_registration',
    'crispy_forms',
    'compressor',
    'sass_processor',
    'leaflet',

    # app
    'app.core',
    'app.account',
    'app.dashboard',
    'app.sentinel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lt_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR),
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'lt_template.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': _PROJECT_NAME,
        'PORT': 5432,
        'USER': _PROJECT_NAME,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#  ########################################   ##
#                   AUTH                      ##
#  ########################################   ##
AUTH_USER_MODEL = 'account.Account'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'


#  ########################################   ##
#                   STATIC                    ##
#  ########################################   ##

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_src"),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
    'sass_processor.finders.CssFinder',
)

#  ########################################   ##
#                   MEDIA                     ##
#  ########################################   ##

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#  ########################################   ##
#                   LIBSASS                   ##
#  ########################################   ##

SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "static_src")
SASS_PROCESSOR_AUTO_INCLUDE = False
SASS_PRECISION = 8
SASS_PROCESSOR_ENABLED = True
SASS_OUTPUT_STYLE = 'compressed'

#  ########################################   ##
#              CRISPY-FORMS                   ##
#  ########################################   ##

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#  ########################################   ##
#              SENTINEL-HUB                   ##
#  ########################################   ##

SH_CLIENT_ID = '31d94b8d-1a1f-45ce-aee3-e708d69cf0f5'
SH_CLIENT_SECRET = 'AnpU5L9fv{GL?fD4.tjiwBtpNV{jv_+@h4!Ih>b.'

#  ########################################   ##
#              DJANGO-LEAFLET                 ##
#  ########################################   ##

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (64.12, 88.2),
    'DEFAULT_ZOOM': 4,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,

    # 'DEFAULT_PRECISION': 12,
}

try:
    from .local_settings import *
except ImportError:
    pass