from .serializers import ProductSerializer, OrderSerializer
from .models import Product, Order
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .filters import ProductFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import time


class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    ordering_fields = ["price"]
    pagination_class = ProductPagination

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @method_decorator(cache_page(60 * 1, key_prefix="products_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        product_id = self.request.query_params.get("id")
        if product_id:
            return Product.objects.filter(id=product_id)
        return Product.objects.order_by("id")


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    @method_decorator(cache_page(60 * 1, key_prefix="order"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        qs = Order.objects.prefetch_related("items__product", "user")
        return qs

    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)
