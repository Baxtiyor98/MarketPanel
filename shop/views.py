from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import *

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers

class ProductsAPIView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class CasherAPIView(viewsets.ModelViewSet):
    queryset = Casher.objects.all()
    serializer_class = CasherSerializers

class SaleAPIView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializers

class CardAPIView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

    # def list(self, request, *args, **kwargs):
    #
    #     return Response({'message':'Ok'})

class VolumeAPIView(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializers

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
