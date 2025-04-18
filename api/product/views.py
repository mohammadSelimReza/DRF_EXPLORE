from .serializers import ProductSerializer,OrderSerializer
from .models import Product,Order
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()    
    

class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product','user')
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)