import json
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import datetime
from telegram.models import Update, Message, Contact
import requests
from rich import print

# Create your views here.
class GetUpdate(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    def post(self,request,format=None):
        jsondata = dict(request.data)
        jsondata["timestamp"] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        
        obj = {
            "update_id":jsondata["update_id"],
            "message_id":jsondata["message"]["message_id"],
            "sender_id":jsondata["message"]["from"]["id"],
            "sender_is_bot":jsondata["message"]["from"]["is_bot"],
            "sender_username":jsondata["message"]["from"]["username"],
            "chat_id":jsondata["message"]["chat"]["id"],
            "date":datetime.datetime.fromtimestamp(jsondata["message"]["date"])
        }
        
        contactObj = None
        
        if obj.get("text",None):
            if obj["text"][0] == "/":
                obj["bot_command"]=True
            else:
                obj["bot_command"]=False
        else:
            obj["bot_command"]=False
        
        if jsondata["message"].get("reply_to_message",None):
            obj["reply_to_message_id"] = jsondata["message"]["reply_to_message"]["message_id"]
            
        if jsondata["message"].get("text",None):
            obj["text"] = jsondata["message"]["text"]
        
        if jsondata["message"].get("contact",None):
            #obj["contact_phone_number"]=jsondata["message"]["contact"]["phone_number"]
            #obj["contact_user_id"]=jsondata["message"]["contact"]["user_id"]
            #obj["contact_first_name"]=jsondata["message"]["contact"]["first_name"]
            #obj["contact_last_name"]=jsondata["message"]["contact"]["last_name"]
            contactObj = jsondata["message"]["contact"]
        
        upd, _ = Update.objects.get_or_create(
            update_id=obj["update_id"],
            defaults=obj
        )
        
        if upd.text == "/start":
            self.start_command(upd)
        elif upd.text == "/help":
            self.help_text(upd)
        
        if contactObj:
            theContact = Contact.objects.update_or_create(
                user_id=contactObj["user_id"],
                defaults={
                    "phone_number":contactObj["phone_number"],
                    "first_name":contactObj["first_name"],
                    "last_name":contactObj["last_name"]
                }
            )
            payload = {
                "chat_id":upd.chat_id,
                "text":"Contact saved!",
                "reply_to_message_id":upd.message_id
            }
            res = requests.post(f"{settings.TELEGRAM_BASE}/sendMessage", json=payload)
            jsondata = res.json()
            
            self.save_message(jsondata,upd)
            
        return Response(obj)
    
    def save_message(self,jsondata,update:Update):
        
        obj = {
            "message_id":jsondata["result"]["message_id"],
            "sender_id":jsondata["result"]["from"]["id"],
            "sender_is_bot":jsondata["result"]["from"]["is_bot"],
            "sender_username":jsondata["result"]["from"]["username"],
            "chat_id":jsondata["result"]["chat"]["id"],
            "date":datetime.datetime.fromtimestamp(jsondata["result"]["date"]),
            "text":jsondata["result"]["text"],
            "reply_to_message_id":update.message_id
        }
        
        msg = Message.objects.create(**obj)
        msg.save()
    
    def start_command(self,update:Update):
        message_text="Please share your contact"
        payload = {
            "chat_id":update.chat_id,
            "text":message_text,
            "reply_to_message_id":update.message_id,
            "reply_markup":{
                "force_reply":True,
                "one_time_keyboard":True,
                "keyboard":[
                    [
                        {"text":"Share contact","request_contact":True}
                    ],
                    ["Cancel"]
                ]
            }
        }
        res = requests.post(f"{settings.TELEGRAM_BASE}/sendMessage", json=payload)
        jsondata = res.json()
        
        self.save_message(jsondata,update)
    
    def help_text(self,update:Update):
        pass