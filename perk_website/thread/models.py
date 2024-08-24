from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
# Create your models here.


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return self.title
       
    def get_absolute_url(self): # Change here
        return reverse('post-detail', kwargs={'pk': self.pk})
       
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    
class Maps(models.Model):
    map_name = models.CharField(max_length=100)
    wonder_weapon = models.CharField(max_length=100)
    easter_egg = models.CharField(max_length=10)
    video_guide = models.ImageField()
    
    def __str__(self):
        return self.map_name
    
    

    

       