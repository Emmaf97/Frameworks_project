from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Steve K',
        'title': 'First Blog Post',
        'content': 'Content for the first post.',
        'date_posted': '12/07/2023'
    },

     {
        'author': 'Scott K',
        'title': 'Second Blog Post',
        'content': 'Content for the second post.',
        'date_posted': '13/07/2023'
    }

]
def home(request):
   context = {
        'posts': posts
            }
   return render(request, 'thread/home.html',context)

def about(request):
    return render(request, 'thread/about.html',{'title': 'About'})
   
def league(request):
    return render(request, 'thread/league.html')
   
def store(request):
    return render(request, 'thread/store.html')
   
def thread(request):
    return render(request, 'thread/thread.html')

def contact(request):
    return render(request, 'thread/contact.html')
   


