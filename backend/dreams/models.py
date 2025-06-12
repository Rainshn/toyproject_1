from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class DreamKeyword(models.Model): # 키워드
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class DreamRecord(models.Model): # 꿈 기록
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    context = models.TextField()
    tags = models.CharField(max_length=100) # 쉼표 구분 태그
    feelings = models.CharField(max_length=100, blank=True) # 쉼표 구분 감정
    created_at = models.DateTimeField(auto_now_add=True)

