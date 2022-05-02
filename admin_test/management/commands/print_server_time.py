from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Показывает время сервера"

    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write(f"Время сервера {time}")
