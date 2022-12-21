from django.db import models

# Create your models here.
class Art(models.Model):
    image=models.ImageField(upload_to="arts")
    caption=models.CharField(max_length=255)
    price=models.FloatField(default=0.0)
    available=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.image.name} - {self.caption}"

class Customer(models.Model):
    phone=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=200,default="Anonymous")
    
    def __str__(self) -> str:
        return f"{self.phone}|{self.name}"

class ArtOrder(models.Model):
    arts=models.ManyToManyField(Art,related_name="art_orders")
    customer=models.ForeignKey(Customer,related_name="art_orders",on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)