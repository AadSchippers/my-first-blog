from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, PostComment
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

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
          comment.author = request.user
          comment.save()
          return redirect('post_detail', pk=pk)
    else:
       form = PostComment()
    return render(request, 'blog/post_comment.html', {'form': form})
