from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost

# Create your views here.
def posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts.html', {'posts':posts})

def postPage(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/postPage.html', {'post':post})

@login_required(login_url='/users/login')
def newPost(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect('posts:list')
    else:
        form = CreatePost()
    return render(request, 'posts/newPost.html', {'form':form})