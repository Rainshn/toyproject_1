from django.db import models
from dreams.models import DreamRecord

# Create your models here.
class Interpret(models.Model):
    dreamRecord = models.OneToOneField(DreamRecord, on_delete=models.CASCADE)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)