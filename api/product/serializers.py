from rest_framework import serializers
from .models import Product,Order,OrderItem
class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','info','price','quantity','in_stock']

    def validate_price(self,value):
        """
        Product Price should be non-negative(positive)
        """
        if value < 0:
            raise serializers.ValidationError("Price can't be Negative")
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    class Meta:
        model = OrderItem
        fields = ['product_name','quantity',"item_subtotal"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    user_name = serializers.SerializerMethodField()
    total_bill = serializers.SerializerMethodField()
    def get_user_name(self,obj):
        return obj.user.username
    def get_total_bill(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    class Meta:
        model = Order
        fields = [
            "order_id",
            "user_name",
            "status",
            "items",
            "total_bill",
        ]