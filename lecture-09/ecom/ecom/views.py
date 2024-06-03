from django.http import HttpResponse
from rest_framework.views import APIView
from ecom.models import Product
from ecom.serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class EmptyException(Exception):
    pass


class ProductListCreateAPIView(APIView):
    def get(self):

        products = Product.objects.all()

        if len(products) == 0:
            raise EmptyException()

        return ProductSerializer(products, many=True)


