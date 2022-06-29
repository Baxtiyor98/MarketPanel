from rest_framework import serializers
from .models import *

class VolumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CasherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Casher
        fields = '__all__'

class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SaleHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SaleHistory
        fields = '__all__'

class PriceHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = '__all__'

