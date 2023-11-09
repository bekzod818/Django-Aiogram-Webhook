from django.contrib import admin
from tgbot.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "username", "tg_id", )
    fields = ("full_name", "username", "tg_id", )
