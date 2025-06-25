from django.shortcuts import render, redirect 
from .forms import *
from blog.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
    
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    
    return render(request, 'accounts/signup.html', {'form':form})
    
    
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()})
    
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        auth_login(request, form.user_cache)
        return redirect('blog:list')
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('blog:list')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def user_info(request):
    if request.method=="POST":
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            request.user.profile_image.delete()
            request.user.profile_image = profile_image
            request.user.save()
            
            
    return render(request, 'accounts/user_info.html')

def myblog(request):
    #posts = request.user.posts.all().order_by('-id') 정참조 방식 
    posts = Post.objects.filter(author=request.user).order_by('-id') #filter메소드 사용 
    return render(request, 'accounts/myblog.html', {'posts': posts})

def mylike(request):
    # posts = Post.objects.all().order_by('-id')
    #liked_posts = [post for post in posts if request.user in post.like.all()]
    # 역참조 코드 : liked_posts = request.user.like_posts.all().order_by('-id')
    liked_posts = Post.objects.filter(like=request.user).order_by('-id')
    return render(request, 'accounts/mylike.html', {'liked_posts': liked_posts})
