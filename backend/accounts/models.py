from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=10, null=True, blank=True)

    ## 약관 동의 관련 필드
    terms_agreed = models.BooleanField(default=False)
    privacy_agreed = models.BooleanField(default=False)
    age_confirmed = models.BooleanField(default=False)
    marketing_agreed = models.BooleanField(default=False) # 선택 약관