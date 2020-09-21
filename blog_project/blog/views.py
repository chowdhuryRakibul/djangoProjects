from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BlogListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'
    #context_object_name = 'myPost'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
