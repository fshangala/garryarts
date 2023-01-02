from django.db import models

# Create your models here.
class Contact(models.Model):
    user_id=models.BigIntegerField(unique=True)
    username=models.CharField(max_length=200,unique=True,null=True)
    phone_number=models.CharField(max_length=200,null=True)
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    staff=models.BooleanField(default=False)

class Update(models.Model):
    update_id=models.BigIntegerField(unique=True)
    message_id=models.BigIntegerField(unique=True)
    sender_id=models.BigIntegerField()
    sender_is_bot=models.BooleanField()
    sender_username=models.CharField(max_length=200)
    chat_id=models.BigIntegerField()
    date=models.DateTimeField()
    reply_to_message_id=models.BigIntegerField(null=True)
    text=models.TextField(null=True)
    bot_command=models.BooleanField()
    
    def __str__(self) -> str:
        return str(self.update_id)+" "+self.text

class Message(models.Model):
    message_id=models.BigIntegerField(unique=True)
    sender_id=models.BigIntegerField()
    sender_is_bot=models.BooleanField()
    sender_username=models.CharField(max_length=200)
    chat_id=models.BigIntegerField()
    date=models.DateTimeField()
    reply_to_message_id=models.BigIntegerField(null=True)
    text=models.TextField(null=True)
    
    def __str__(self) -> str:
        return str(self.message_id)+" "+self.text
    
    