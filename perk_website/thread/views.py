from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Contact, Maps
from django.contrib import messages #import for messages
from .forms import ContactForm
from store.models import Products
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import json
import os
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView  
)


class PostListView(ListView):
     model = Post
     template_name = 'thread/thread.html'
     context_object_name = 'posts'
     ordering = ['-date_posted']
     paginate_by = 5
     
class PostDetailView(DetailView):
    model = Post  

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
     
    #Overriding form_valid method 
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # New class created and UpdateView passed in.
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       
    def test_func(self):
        post = self.get_object()
        # Check if the current user is the author of the post
        return post.author == self.request.user
       
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # New class PostDeleteView created here
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
       
    def test_func(self):
        post = self.get_object()
        # Check if the current user is the author of the post
        return post.author == self.request.user
       
                  
def home(request):
    return render(request, 'thread/home.html')

def about(request):
    return render(request, 'thread/about.html',{'title': 'About'})
   
def league(request):
    return render(request, 'thread/league.html')

def maps(request):
    context ={
        'maps': Maps.objects.all()
    }
    return render(request, 'thread/maps.html', context)
   
def store(request):
    context ={
        'products': Products.objects.all()
    }
    return render(request, 'thread/store.html', context)
    
    
def thread(request):
    context = {
       'posts': Post.objects.all()
        }
    return render(request, 'thread/thread.html', context)

def contact(request):
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Contact form successfully submitted, our team will contact you shortly.')
            return redirect('home')
    else:
        c_form = ContactForm()

    context = {
        'c_form': c_form
    }

    return render(request, 'thread/contact.html', context)
   


