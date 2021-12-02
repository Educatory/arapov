import logging

logging.basicConfig()  # сбрасываем настройки логирования

DEBUG = True
INTERNAL_IPS = ('127.0.0.1', 'localhost')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES
from .settings import DATABASES  # noqa

DATABASES['default']['HOST'] = 'db1.siteedu.ru'
DATABASES['default']['NAME'] = 'hack'
DATABASES['default']['PORT'] = '6120'
DATABASES['default']['USER'] = 'hack'
DATABASES['default']['PASSWORD'] = ''

