from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts') #User 모델 참조 
    is_anonymous = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.author}] {self.title}'
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments') #Post 모델 참조 
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments') #User 모델 참조 
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.author}] {self.content}'