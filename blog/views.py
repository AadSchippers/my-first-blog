from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, PostComment, RegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core import validators
from django import forms
from django.utils.translation import gettext as _


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('created_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

@login_required(login_url='/login/')
def post_new(request):
    form = PostForm()
    if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('post_detail', pk=post.pk)
    else:
       form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_new(request, pk):
    form = PostComment()
    if request.method == "POST":
       form = PostComment(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.post = Post.objects.get(pk=pk)
          if request.user.is_authenticated:
              comment.author = request.user
          comment.save()
          return redirect('post_detail', pk=pk)
    else:
       form = PostComment()
    return render(request, 'blog/post_comment.html', {'form': form})

def bloglogout(request):
    logout(request)
    return redirect('post_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
