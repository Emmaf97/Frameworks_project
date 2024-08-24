import json
from django.core.management.base import BaseCommand
from store.models import Products

class Command(BaseCommand):
    help = 'Load products from a JSON file into the database'

    def handle(self, *args, **kwargs):
        # Open the JSON file and load the data
        Products.objects.all().delete()
        
        with open('store/data/products.json', 'r') as file:
            data = json.load(file)
        
        # Access the list of products within the "products" key
        products_data = data.get('products', [])

        for product_data in products_data:
            # Check if the product already exists based on a unique field, such as 'item_name'
            existing_product = Products.objects.filter(item_name=product_data['item_name']).first()

            if existing_product:
                # Delete the existing product
                existing_product.delete()
                print(f"Deleted existing product: {existing_product.item_name}")

            # Now create a new entry
            new_product = Products(
                item_name=product_data['item_name'],
                description=product_data['description'],
                colour=product_data['colour'],
                quantity=product_data['quantity'],
                image=product_data['image']
            )
            new_product.save()
            print(f"Created new product: {new_product.item_name}")

        print("Database updated: old entries deleted and new entries created.")