"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!9sn1*e@gl9s8kfrk+#py9*o6vo69(vbpw+rulokp-p_c^g35s'

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
    "debug_toolbar",
    'ckeditor',
    'news.apps.NewsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
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

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite',
    }
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'NewsPortal/static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}