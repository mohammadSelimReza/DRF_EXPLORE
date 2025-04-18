from django.urls import path
from api.product import views as product_view
from api.user import views as user_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # jwt token:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # registration:
    path("api/user/registration/",user_view.CreateUserAPIView.as_view(),name="registration"),
    # product:
    path("product/list/",product_view.ProductList.as_view()),
    path("product/detail/<str:id>/",product_view.ProductDetailsView.as_view()),
    path("order/list/",product_view.OrderListView.as_view()),
]
