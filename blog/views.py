# from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post

# Create your views here.

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False) # The commit=False prevents it to save into the database
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    form = CommentForm

    return render(request, 'blog/detail.html', {'post': post, 'form': form})