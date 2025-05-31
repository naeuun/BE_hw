from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts') #User 모델 참조 
    is_anonymous = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(User, through="Like", related_name="like_posts")
    scrap = models.ManyToManyField(User, through="Scrap", related_name="scrap_posts")
    
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
    
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_categories")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_categories")

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_scraps")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_scraps")