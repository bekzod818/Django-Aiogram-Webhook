from asgiref.sync import async_to_sync
from tgbot.webhook import proceed_update
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


def home(request: HttpRequest):
    return HttpResponse('Hello world')


@csrf_exempt
def telegram(request: HttpRequest):
    try:
        async_to_sync(proceed_update)(request)
    except Exception as e:
        print(e)
    return HttpResponse()
