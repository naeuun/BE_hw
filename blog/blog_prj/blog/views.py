from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    posts=Post.objects.all().order_by('-id') # id를 역순으로 정렬 (최신글부터 볼 수 있게 됨됨)
    return render(request, 'blog/list.html', {'posts' : posts })

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user
        )
        
        return redirect('blog:list')
    return render(request, 'blog/create.html')

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