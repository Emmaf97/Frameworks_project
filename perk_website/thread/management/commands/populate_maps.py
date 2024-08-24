import json
from django.core.management.base import BaseCommand
from thread.models import Maps

class Command(BaseCommand):
    help = 'Load maps from a JSON file into the database'

    def handle(self, *args, **kwargs):
        # Open the JSON file and load the data
        with open('thread/data/maps.json', 'r') as file:
            data = json.load(file)
        
        maps_data = data.get('zombie_maps', [])

        for map_data in maps_data:
            
            existing_map = Maps.objects.filter(map_name=map_data['map_name']).first()

            if existing_map:
               
                existing_map.delete()
                print(f"Deleted existing product: {existing_map.map_name}")

           
            new_Map = Maps(
                map_name=map_data['map_name'],
                wonder_weapon=map_data['wonder_weapon'],
                easter_egg=map_data['easter_egg'],
                video_guide=map_data['video_guide'],
            )
            new_Map.save()
            print(f"Created new map: {new_Map.map_name}")

        print("Database updated: old entries deleted and new entries created.")