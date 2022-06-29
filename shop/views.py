from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import *

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers

class ProductsAPIView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

    def list(self, request, *args, **kwargs):
        if request.data:
            try:
                name = request.data['name']
                product = Products.objects.filter(Q(name__contains=name))
            except:
                shtrix = request.data['shtrix']
                product = Products.objects.filter(Q(shtrix_code__contains=shtrix))
        else:
            product = Products.objects.all()
        context = [{"id": i.id, 'name': i.name,"price": i.price_with_discount,"shtrix":i.shtrix_code} for i in product]
        return Response(context)

class CasherAPIView(viewsets.ModelViewSet):
    queryset = Casher.objects.all()
    serializer_class = CasherSerializers

class SaleAPIView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializers

    def create(self, request, *args, **kwargs):
        sales = Sale.objects.filter(payment='').order_by('id')
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if len(sales)<3:
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                for i in sales:
                    if not Card.objects.filter(sale_id=int(i.id)):
                        return Response({'sale_id':i.id}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        for i in Card.objects.filter(sale_id=kwargs['pk']): i.delete()
        return Response({'sale_id':kwargs['pk']})

class CardUpdateAPIView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializers
    http_method_names = ['put']

    def update(self, request, *args, **kwargs):
        card_product = Card.objects.get(id=kwargs['pk'])
        quantity = int(request.data['quantity'])
        card_product.add_quantity(quantity)
        return Response(status=status.HTTP_200_OK)

class CardAPIView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

    def list(self, request, *args, **kwargs):
        if request.data:
            sale_id = request.data['sale_id']
            try:
                card_id = request.data['card_id']
                card_product = Card.objects.get(id=int(card_id))
                if request.data['status']=='add':
                    card_product.add
                elif request.data['status']=='sub':
                    if card_product.quantity >1:
                        card_product.sub
            except:
                pass
            card = Card.objects.filter(sale_id=sale_id).order_by('-id')
        else:
            card = Card.objects.all().order_by('-id')
        context = [{"id":i.id,'sale':i.sale.id,"product_id":i.product.id,'name':i.product.name,"quantity":i.quantity,"price":i.product.price_with_discount*i.quantity} for i in card]
        return Response({'total':sum(card.values_list('sold_price',flat=True)),'products':context},status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        # seller = request.data['seller']
        shtrix = request.data['shtrix']
        sale_id = request.data['sale_id']
        try:
            product = Products.objects.get(shtrix_code=shtrix)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Card.objects.create(sale_id=sale_id,product=product,sold_price=product.price_with_discount)
        card = Card.objects.filter(sale_id=sale_id).order_by('-id')
        context = [{"id":i.id,"product_id":i.product.id,'name':i.product.name,"price":i.product.price_with_discount*i.quantity} for i in card]
        return Response(context)

    def update(self, request, *args, **kwargs):
        card_products = Card.objects.filter(sale_id=int(kwargs['pk']))
        for i in card_products:
            i.delete()
        return Response(status=status.HTTP_200_OK)

class VolumeAPIView(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializers

class PriceHistoryAPIView(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializers

    def create(self, request, *args, **kwargs):
        instence = Products.objects.get(id=int(request.data['product']))
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if int(instence.price) != int(request.data['new_price']):
                serializer.save()
                try:
                    instence.price = serializer.data['new_price']
                    instence.save()
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                return Response({'message':"Ok"},status=status.HTTP_200_OK)
            return Response({'message':"Not changed"},status=status.HTTP_403_FORBIDDEN)




