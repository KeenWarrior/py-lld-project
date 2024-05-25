from rest_framework import serializers

from ecomapp.models import Product, DiaryProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class DairyProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaryProduct
        fields = '__all__'

