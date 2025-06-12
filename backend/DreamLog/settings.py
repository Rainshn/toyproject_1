import os
from pathlib import Path

from allauth.socialaccount.apps import SocialAccountConfig
from decouple import config
from django.conf.global_settings import LOGOUT_REDIRECT_URL

import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

AUTH_USER_MODEL = 'accounts.CustomUser'

# 신규 소셜 회원가입 시 리디렉션될 URL
SOCIALACCOUNT_ADAPTER = 'accounts.adapters.MySocialAccountAdapter'

# 중간 기본 페이지 없이 바로 구글 인증 화면으로 이동
SOCIALACCOUNT_LOGIN_ON_GET = True  # 로그인 흐름 단순화

# 로그인 직후 리디렉션되는 기본 경로
LOGIN_REDIRECT_URL = '/accounts/signup_google/'  # 로그인 성공 시 이동 경로


# ## 구글 로그인 리다이렉트
# LOGIN_REDIRECT_URL = '/accounts/signup_google/'

# Application definition

INSTALLED_APPS = [
    # django Cors 관련
    'corsheaders',
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
    'corsheaders.middleware.CorsMiddleware', # Cors (상단에 위치해야 함)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware', # django-allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Cors 허용 도메인(출처 허용, 개발용)
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# 쿠키 인증
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False


# HTTP methods 추가
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT"
)

# 필요 헤더 추가
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

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



WSGI_APPLICATION = 'DreamLog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

## 사용할 데이터베이스 설정
## .env 파일 내용 수정 필요
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
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
            'response_type': 'code', # response_type 파라미터 받기
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
