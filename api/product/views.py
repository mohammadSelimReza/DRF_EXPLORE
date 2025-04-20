from .serializers import ProductSerializer, OrderSerializer
from .models import Product, Order
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .filters import ProductFilter


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        product_id = self.request.query_params.get("id")
        if product_id:
            return Product.objects.filter(id=product_id)
        return Product.objects.all()


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product", "user")
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)
