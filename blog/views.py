from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
#def blog(request):
#    return render(request, 'blog.html', {})

class blogList(ListView):
    model = Post
    template_name = "blog.html"
