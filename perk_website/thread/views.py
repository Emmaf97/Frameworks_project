from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from store.models import Products
from django.conf import settings
import json
import os

def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'thread/home.html', context)

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
    return render(request, 'thread/thread.html')

def contact(request):
    return render(request, 'thread/contact.html')
   


