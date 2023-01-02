from django.contrib import admin
from .models import (
    Update,
    Message,
    Contact
)

# Register your models here.
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display=["update_id","sender_id","sender_username","bot_command","date"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=["message_id","sender_username","date"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["user_id","phone_number","first_name","last_name"]