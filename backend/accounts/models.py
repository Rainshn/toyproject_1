from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Post(models.Model):
    # email = models.EmailField(max_length=30) # 최대 30자 입력
    password = models.TextField(max_length=16)
    username = models.TextField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=10)

    ## 약관 동의 관련 필드
    terms_agreed = models.BooleanField(default=False)
    privacy_agreed = models.BooleanField(default=False)
    age_confirmed = models.BooleanField(default=False)
    marketing_agreed = models.BooleanField(default=False) # 선택 약관