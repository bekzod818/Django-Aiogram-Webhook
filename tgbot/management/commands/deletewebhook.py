import requests
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Deleting webhook'

    def handle(self, *args, **options):
        webhook = requests.get(settings.TELEGRAM_API_BASE_URL + "getWebhookInfo").json()
        if webhook.get("result", "").get("url", "") == "":
            self.stdout.write(self.style.NOTICE("Webhook have not set yet!"))
        else:
            url = f"{settings.TELEGRAM_API_BASE_URL}deleteWebhook"
            requests.post(url)
            self.stdout.write(self.style.SUCCESS('Webhook was successfully deleted!'))
