from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=30, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.username 