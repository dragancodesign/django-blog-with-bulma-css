from django.db.models import Q # This allows us to search in multiple fields !!!
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post, Category

# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE) # Here added active status

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

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)) 
# Q imported to search in multiple fields and " | " means OR !!! 
# QUESTION = PROBLEM: It displays posts that have CHOICES_STATUS = DRAFT !!!

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})