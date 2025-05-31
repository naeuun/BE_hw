from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required


def main(request):
    categories = Category.objects.all()
    category_posts = [ (category, category.posts.all().order_by('-id')[:4]) for category in categories]

    return render(request, 'posts/main.html', {'categories':categories, 'category_posts':category_posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {'post':post})

@login_required
def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        Comment.objects.create(
            post=post,
            content=content,
            author=request.user,
            is_anonymous = is_anonymous
        )   
        return redirect('posts:detail', id)
    return redirect('posts:main')

def update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method =='POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') =='on'
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def delete(reqeust, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:main')

def delete_comment(reqeust, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    post_id= comment.post.id
    return redirect('posts:detail', post_id)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        post = Post.objects.create(
            title = title,
            content = content,
            is_anonymous = is_anonymous,
            author=request.user
        )
        
        post.category.add(category)
        
        return redirect('posts:category', slug)
    return render(request, 'posts/category.html', {'posts':posts, 'category':category})
    
def like(request, post_id): 
    if request.method =="POST":
        post = get_object_or_404(Post, id=post_id)
        user = request.user
            
        if user in post.like.all():
            post.like.remove(user)
        else:
            post.like.add(user)
        return redirect('posts:detail', post_id)
    
def scrap(request, post_id): 
    if request.method =="POST":
        post = get_object_or_404(Post, id=post_id)
        user = request.user
            
        if user in post.scrap.all():
            post.scrap.remove(user)
        else:
            post.scrap.add(user)
        return redirect('posts:detail', post_id)