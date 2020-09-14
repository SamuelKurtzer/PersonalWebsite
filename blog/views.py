from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class blogList(ListView):
    model = Post
    template_name = "blogList.html"

class blogPost(DetailView):
    model = Post
    template_name = "blogPost.html"
