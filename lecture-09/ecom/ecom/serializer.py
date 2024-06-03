from ecom.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
