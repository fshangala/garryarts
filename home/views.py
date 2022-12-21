from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from . import models
from .serializers import (
    ArtSerializer,
    ArtOrderSerializer
)

# Create your views here.
class HomeView(ListView):
    model=models.Art
    context_object_name="arts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["arts"] = ArtSerializer(context["arts"],many=True).data
        return context

class PlaceOrderView(TemplateView):
    template_name="home/placeOrder.html"
    
    def post(self,request):
        data = dict(request.POST)
        info = {
            "phone":request.POST["phone"],
            "name":request.POST["name"],
            "arts":[x for x in data["arts"]]
        }
        
        customer,createdCustomer = models.Customer.objects.get_or_create(phone=info["phone"],defaults={"name":info["name"]})
        if not createdCustomer:
            customer.name = info["name"]
            customer.save()
        artorder = models.ArtOrder.objects.create(customer=customer)
        artorder.save()
        for art in info["arts"]:
            artorder.arts.add(art)

        return render(request,self.template_name,{"artOrder":artorder})
    