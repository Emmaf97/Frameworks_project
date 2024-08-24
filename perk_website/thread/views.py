from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Contact
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
    # context = {
    #    'posts': Post.objects.all()
    # }
    return render(request, 'thread/home.html')

def about(request):
    return render(request, 'thread/about.html',{'title': 'About'})
   
def league(request):
    return render(request, 'thread/league.html')
   
def store(request):
    # Load data from JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'store', 'data', 'products.json')
    # json_file_path = os.path.join(os.path.dirname(__file__), 'store', 'data', 'products.json')
    
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return render(request, 'thread/store.html', {'error': 'File not found'})
    except json.JSONDecodeError:
        return render(request, 'thread/store.html', {'error': 'Error decoding JSON'})
    
    # Debug: Print data to check its structure
    print("Loaded data:", data)
    
    # Ensure data is a dictionary with a 'products' key
    if isinstance(data, dict) and 'products' in data:
        products_data = data['products']
        if isinstance(products_data, list):
            products = []
            for item in products_data:
                # Debug: Print each item to check its structure
                print("Processing item:", item)
                
                if isinstance(item, dict):
                    product = Products.objects.create(
                        item_name=item.get('item_name'),
                        description=item.get('description'),
                        colour=item.get('colour'),
                        quantity=item.get('quantity'),
                        image=item.get('image')  # Ensure this path is correct
                    )
                    products.append(product)
                else:
                    return render(request, 'thread/store.html', {'error': 'Invalid data format in products list'})
        else:
            return render(request, 'thread/store.html', {'error': 'Invalid JSON format for products'})
    else:
        return render(request, 'thread/store.html', {'error': 'Invalid JSON structure'})
    
    return render(request, 'thread/store.html', {'products': products})
   
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
   


