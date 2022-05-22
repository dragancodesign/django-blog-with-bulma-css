from django.shortcuts import render
from django.shortcuts import redirect # I have added

# from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

