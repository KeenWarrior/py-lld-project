from rest_framework.response import Response
from rest_framework.views import APIView
from ecomapp.models import Product
from ecomapp.models import DiaryProduct
from ecomapp.serializers import ProductSerializer
from ecomapp.serializers import DairyProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateProductAPIView(APIView):

    def get(self, request):
        # products = Product.objects.all().filter(price__range=[60.0, 100.0])

        products = Product.objects.raw('SELECT * FROM ecomapp_product WHERE price BETWEEN 60.0 AND 100.0')

        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=200)

    def post(self, request):
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=400)

        decoded_data.save()

        return Response(decoded_data.data, status=201)


class DairyListCreateAPIView(ListCreateAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DairyProductSerializer


class DairyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DairyProductSerializer