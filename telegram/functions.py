from telegram.models import (
    Contact
)
from django.conf import settings
import requests

def send_notification(message):
    contacts = Contact.objects.all()
    for contact in contacts:
        if contact.staff:
            payload = {
                "chat_id":contact.user_id,
                "text":message
            }
            res = requests.post(f"{settings.TELEGRAM_BASE}/sendMessage", json=payload)
            jsondata = res.json()