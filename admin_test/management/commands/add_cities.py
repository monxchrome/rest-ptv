from django.core.management.base import BaseCommand
import json
from admin_test.models import City


class Command(BaseCommand):
    help = "Берем данные из файла cities.json и импортируем в нашу базу данных"

    def handle(self, *args, **options):
        with open('data/cities.json', 'r', encoding='utf-8') as f:
            cities = json.load(f)
            for city in cities:
                new_city, created = City.objects.get_or_create(
                    title=city.get('title'), description=city.get('description')
                )
                if not created:
                    print(f"город {new_city} уже в БД")
