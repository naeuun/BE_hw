from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length = 10)
    phone_num = models.CharField(max_length = 11)
    email = models.EmailField(max_length = 50)
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.name