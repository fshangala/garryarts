from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from . import models
from .serializers import (
    ArtOrderSerializer
)

class ArtOderView(APIView):    
    def get(self,request):
        artOrders = ArtOrderSerializer(models.ArtOrder.objects.all(),many=True)
        return Response(artOrders.data)
    
    def post(self,request,format=None):
        return Response(request.data)