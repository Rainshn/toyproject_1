from pathlib import Path

from allauth.socialaccount.apps import SocialAccountConfig
from decouple import config
from django.conf.global_settings import LOGOUT_REDIRECT_URL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'accounts.CustomUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'dreams',
    'interpretation',
    'main',
    # django-allauth 관련
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # 'accounts.email_auth.EmailAuth',
    'django.contrib.auth.backends.ModelBackend', # 기본 인증
    'allauth.account.auth_backends.AuthenticationBackend', # allauth 인증
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware', # django-allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DreamLog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

## 구글 로그인 리다이렉트
LOGIN_REDIRECT_URL = '/accounts/signup_google/'

# 중간 기본 페이지 없이 바로 구글 인증 화면으로 이동
SOCIALACCOUNT_LOGIN_ON_GET = True

WSGI_APPLICATION = 'DreamLog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

## Django 기본 비밀번호 검증기
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

## django-allauth의 구글 로그인 세부 설정 정의
SOCIALACCOUNT_PROVIDERS = {
    'google': { # 구글 소셜 로그인 의미
        'APP': { # 구글 OAuth 2.0(구글 클라우드)에서 발급받은 인증 정보
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': ''
        },
        'SCOPE': [ # 구글에서 요청할 사용자 권한 범위 지정
            'profile', # 사용자의 기본 프로필(이름, 사진 등)
            'email', # 사용자의 이메일 주소
        ],
        'AUTH_PARAMS': { # 인증 요청 시 구글에 전달할 추가 파라미터
            'access_type': 'online', # 사용자가 온라인 상태에서 인증 의미
            'prompt': 'select_account', # 강제로 계정 선택창 띄우기(기본 창 건너뜀)
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
