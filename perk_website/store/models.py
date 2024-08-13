from django.db import models

# Create your models here.
class Products(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    colour = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.item_name