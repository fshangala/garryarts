from django.test import TestCase
from rest_framework.test import APITestCase
from .models import (
    Contact,
    Update,
    Message
)
from rich.console import Console
from rich import print

console = Console()
defaultSpinner="bouncingBall"

# Create your tests here.
class TelegramTests(APITestCase):
    def test_get_version(self):
        """
        Text getting the api version
        """
        with console.status("Test 1: Getting the API version",spinner=defaultSpinner):
            response = self.client.get("/version/")
            console.print(response.content,style="green")
    
    def test_start_command(self):
        """
        Test the /start command
        """
        with console.status("Test 2: Sending /start command",spinner=defaultSpinner):
            data = {
                "update_id": 750960902,
                "message": {
                    "message_id": 1,
                    "from": {
                        "id": 1299181435,
                        "is_bot": False,
                        "first_name": "Funduluka",
                        "last_name": "Shangala",
                        "username": "fshangala",
                        "language_code": "en"
                    },
                    "chat": {
                        "id": 1299181435,
                        "first_name": "Funduluka",
                        "last_name": "Shangala",
                        "username": "fshangala",
                        "type": "private"
                    },
                    "date": 1672578357,
                    "text": "/start",
                    "entities": [
                        {
                            "offset": 0,
                            "length": 6,
                            "type": "bot_command"
                        }
                    ]
                }
            }
            response = self.client.post('/telegram/get-update/',data,format='json')
        
        with console.status("Test 2: Checking for processed information",spinner=defaultSpinner):
            updates = Update.objects.all()
            self.assertGreaterEqual(updates.count(),1)
            console.print("Update saved:",updates.last().update_id,style="green")
    
    def test_send_contact(self):
        """
        Testing sending a contact ot the telegram bot
        """
        with console.status("Test 3: Sending contact",spinner=defaultSpinner):
            data = {
                "update_id": 750960902,
                "message": {
                    "message_id": 1,
                    "from": {
                        "id": 1299181435,
                        "is_bot": False,
                        "first_name": "Funduluka",
                        "last_name": "Shangala",
                        "username": "fshangala",
                        "language_code": "en"
                    },
                    "chat": {
                        "id": 1299181435,
                        "first_name": "Funduluka",
                        "last_name": "Shangala",
                        "username": "fshangala",
                        "type": "private"
                    },
                    "date": 1672578357,
                    "reply_to_message": {
                        "message_id": 5,
                        "from": {
                            "id": 5838379022,
                            "is_bot": True,
                            "first_name": "GarryArts",
                            "username": "garryarts_bot"
                        },
                        "chat": {
                            "id": 1299181435,
                            "first_name": "Funduluka",
                            "last_name": "Shangala",
                            "username": "fshangala",
                            "type": "private"
                        },
                        "date": 1672588449,
                        "text": "Please share your contact"
                    },
                    "contact": {
                        "phone_number": "260974836436",
                        "first_name": "Funduluka",
                        "last_name": "Shangala",
                        "user_id": 1299181435
                    }
                }
            }
            response = self.client.post('/telegram/get-update/',data,format='json')
              
        with console.status("Test 3: Checking for processed information",spinner=defaultSpinner):
            updates = Contact.objects.all()
            self.assertGreaterEqual(updates.count(),1)
            console.print("Saved phone number:",updates.last().phone_number,style="green")
        