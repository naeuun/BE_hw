from django.db import models
from users.models import User
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length = 50)
    content =models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(to=Category, through = "PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="like_posts")
    image = models.ImageField(upload_to=upload_filepath, blank=True)
    video = models.FileField(upload_to=upload_filepath, blank=True)
    
    def __str__(self):
        return f'[{self.id}] {self.title}'
    

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f'[{self.id}] {self.content}'
    

class PostCategory(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_categories")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name = "post_categories")
    
class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_likes")