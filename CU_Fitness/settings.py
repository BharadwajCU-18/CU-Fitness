"""
Django settings for CU_Fitness project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kwwhj2_)&w%m!jc6njjvk9_@l4k7t1ly8qer9)4p0e^)2153qf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personalInfo',
    'chatbot',
    'rest_framework',
    'home',
    'mealSuggestions', 
    'corsheaders',
    'payment',
    'django_extensions',
    'profiles',
    'workoutPlanSuggestions',
    'fitnessProgress',
    'fitnessReport',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'fitnessReport.custom.middleware.convert_exception_to_response'
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'CU_Fitness.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure 'templates' directory is included
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

WSGI_APPLICATION = 'CU_Fitness.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = "/static/"

# STATIC_ROOT = BASE_DIR / 'staticfiles'  


STATICFILES_DIRS = [
     BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = '/personalInfo/login/'

# # settings.py
# GOOGLE_API_KEY = 'AIzaSyAf6Bmb1yEjeNsyEU9SeR-ES1asIp62-TM'  
# # settings.py

# GOOGLE_PROJECT_ID = 'gen-lang-client-0577741848'  
# settings.py

# GOOGLE_OAUTH2_CREDENTIALS_FILE = r'C:\Users\saiku\Downloads\cufitness.json' # Replace with your actual path to the JSON file
# import os

# # This will dynamically build the correct path based on your project directory
# GOOGLE_OAUTH2_CREDENTIALS_FILE = os.path.join(BASE_DIR, 'cufitnesss.json')

# # The redirect URI for OAuth2 (you can use this for authentication)
# GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/oauth2callback/'  # Adjust for production

# # The Google Cloud Project ID for your Dialogflow or other APIs
# GOOGLE_PROJECT_ID = 'gen-lang-client-0577741848'  # Your Dialogflow project ID

# # The API scopes you need
# GOOGLE_API_SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

# # This is the path to your service account file (from previous code, you can rely on the first variable)
# SERVICE_ACCOUNT_FILE = GOOGLE_OAUTH2_CREDENTIALS_FILE

import os 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "api_key")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'helpcufitness@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'axkg wtnt qkya eftj'  # Your email password
DEFAULT_FROM_EMAIL = 'help@cufitness.com'  # Default sender email
