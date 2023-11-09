import requests
from django.core.management.base import BaseCommand
from src.settings import WEBHOOK_URL, TELEGRAM_API_BASE_URL


class Command(BaseCommand):
    help = 'Setting webhook'

    def handle(self, *args, **options):
        webhook = requests.get(TELEGRAM_API_BASE_URL + "getWebhookInfo").json()
        if webhook.get("result", "").get("url", "") != WEBHOOK_URL:
            requests.post(TELEGRAM_API_BASE_URL + "setWebhook", data={"url": WEBHOOK_URL})
            self.stdout.write(self.style.SUCCESS('Webhook was successfully set!'))
        else:
            self.stdout.write(self.style.WARNING('Webhook is already set!'))
