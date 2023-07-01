import tempfile
import os
from pathlib import Path
import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = '=#zaq)7!!1ezyr_vwulv134)jdefd=x$&7l#35483!-p*$k%0o'

ENV = 'Local'

DEBUG = False

DJ_ADMIN_ENABLED = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR/'static'

MEDIA_ROOT = BASE_DIR/'media'

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

LANGUAGE_COOKIE_SECURE = False

SECURE_SSL_REDIRECT = False

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_HSTS_PRELOAD = False

SECURE_HSTS_SECONDS = 15552000
GOOGLE_RECAPTCHA_SECRET_KEY = '6LddL5sfAAAAADA9OwJI0bY5Fl1Lc9JV62Qy9r1t'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TWILIO_ACCOUNT_SID = 'AC5210b926dcfec72faae11ec9b5e93ce8'

TWILIO_AUTH_TOKEN = 'bb1a37dca728d60a3d8c7517976a2cb4'

TWILIO_NUMBER_VERIFICATION_SERVICE_SID = 'VAd87ac08a7d573c564d9d08eadb142f25'



# s = socket.socket()
# host = '192.168.1.1'
# port = 8080
# s.connect((host, port))
# socket.getaddrinfo('localhost',587)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bany@pixelstat.com'
EMAIL_HOST_PASSWORD = '#bany2021'
EMAIL_USE_TLS = True
# SMTP_Authentication: False or none
# SSL_or_Secure Connection: None


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'yojanadb',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
