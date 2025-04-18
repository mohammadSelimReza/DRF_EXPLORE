from django.urls import path
from api.product import views as product_view

urlpatterns = [
    path("product/list/",product_view.product_list),
    path("product/detail/<str:id>/",product_view.product_detail),
    path("order/list/",product_view.order_list),
]
