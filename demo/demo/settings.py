"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ae-lwv$%nelj_axrq1rd5+emb5t_7-i!5_jsr!aas54$h0do(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_richtexteditor',
    'blog',
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

ROOT_URLCONF = 'demo.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Messages framework

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.DEBUG:   'info',
    messages.INFO:    'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR:   'danger',
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/public/static/'
MEDIA_URL = '/public/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

# Absolute paths to the directory where static files and media will be collected.
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')


# Rich Text Editor Config
RICHTEXTEDITOR_CONFIG = {
    # 'ckeditor': {
        # 'v5': {
            # 'balloon': {}
            # 'balloon-block': {}
            # 'classic': {}
            # 'decoupled-document': {}
            # 'inline': {}
        # }
    # }
    # 'ckeditor': {
        # 'v4': {
            # 'basic': {}
            # 'full': {}
            # 'full-all': {}
            # 'standard': {}
            # 'standard-all': {}
        # }
    # }
    'ckeditor': {
        'v5': {
            'classic': {
                'css': {
                    'front': {
                        'theme': os.path.join(STATIC_URL, 'css/ckeditor/v5/front/theme/bootstrap.css'),
                        'custom': os.path.join(STATIC_URL, 'css/ckeditor/v5/front/custom/classic.css'),
                    },
                    # 'admin': {
                        # 'theme': os.path.join(STATIC_URL, 'css/ckeditor/v5/admin/theme/bootstrap.css'),
                        # 'custom': os.path.join(STATIC_URL, 'css/ckeditor/v5/admin/custom/classic.css'),
                    # },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/20.0.0/classic/ckeditor.js',
                    # 'plugins': [],
                    'init-config': os.path.join(STATIC_URL, 'js/ckeditor/v5/classic-config.js'),
                    # 'init-script': os.path.join(STATIC_URL, 'js/ckeditor/v5/classic.js'),
                }
            }
        }
    }
}
