import requests
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Deleting webhook'

    def handle(self, *args, **options):
        url = f"{settings.TELEGRAM_API_BASE_URL}deleteWebhook"
        requests.post(url)
        self.stdout.write(self.style.SUCCESS('Webhook was successfully deleted!'))
