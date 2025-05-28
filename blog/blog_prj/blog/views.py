from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from users.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category).order_by('-id')
        # 원래 코드 : posts = category.posts.all().order_by('-id')
    else:
        posts=Post.objects.all().order_by('-id') # id를 역순으로 정렬 (최신글부터 볼 수 있게 됨)
    return render(request, 'blog/list.html', {'posts' : posts , 'categories' : categories})

@login_required
def create(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]
        
        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user
        )
        
        for category in category_list:
            post.category.add(category)
        
        
        return redirect('blog:list')
    return render(request, 'blog/create.html', {'categories':categories})

def detail(request, id):
    post=get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, id):
    post=get_object_or_404(Post, id=id)
    
    if request.method == "POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('blog:detail',id)
    return render(request, 'blog/update.html', {'post' : post})

def delete(request, id):
    post=get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog:list')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        content = request.POST.get('content')
    
        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('blog:detail', post_id)
    return redirect('blog:list')

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    
    if post in user.like_posts.all(): #정참조 코드 : if user in post.like.all()
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('blog:detail', post_id)