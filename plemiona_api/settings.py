"""
Django settings for plemiona_api project.
"""
from datetime import timedelta
from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", "test")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", True, cast=bool)

ALLOWED_HOSTS = ["*"]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000/",
    "https://api-tribalwars.app/",
    "https://www.api-tribalwars.app/",
]

# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "game",
    "django_extensions",
    "celery",
]

ASGI_APPLICATION = "plemiona_api.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "plemiona_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "plemiona_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# General
APPEND_SLASH = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
USE_I18N = False
USE_L10N = True
USE_TZ = True
LOGIN_REDIRECT_URL = "/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []
STATIC_URL = "/static/"
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user app
# AUTH_USER_MODEL = "users.User"

# Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": int(os.getenv("DJANGO_PAGINATION_LIMIT", 10)),
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    "DEFAULT_RENDERER_CLASSES": ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PARSER_CLASSES": ("djangorestframework_camel_case.parser.CamelCaseJSONParser",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("utils.jwt_authentication.JWTAuthentication",),
    "EXCEPTION_HANDLER": "utils.exception_handler.custom_exception_handler",
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "player_id",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# set the celery broker url
CELERY_BROKER_URL = "redis://localhost:6379/0"

# set the celery result backend
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

# set the celery timezone
CELERY_TIMEZONE = "UTC"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
