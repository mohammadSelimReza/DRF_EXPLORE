from .serializers import ProductSerializer,OrderSerializer
from .models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    print(products)
    serializer = ProductSerializer(products,many=True)
    return Response({'products':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    serializer = ProductSerializer(product)
    # return Response({'product':serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response({'orders':serializer.data},status=status.HTTP_200_OK)
