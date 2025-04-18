from django.db import models
from shortuuid.django_fields import ShortUUIDField
from api.user.models import User
from .utilities import product_image_upload

# Create your models here.
class Product(models.Model):
    id = ShortUUIDField(
        length=8,
        max_length=10,
        alphabet="abcdefg1234567890",
        primary_key=True,
        db_index=True,
    )
    name = models.CharField(max_length=100)
    info = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.PositiveIntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=product_image_upload,blank=True,null=True)
    @property
    def in_stock(self):
        return self.quantity > 0
    
    def __str__(self):
        return f"{self.name} created on : {self.added_on}"
    
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
    order_id = ShortUUIDField(
        length=4,
        max_length=4,
        alphabet="abcdefg1234567890",
        primary_key=True,
        db_index=True,
    )
    user =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    products = models.ManyToManyField(Product, through="OrderItem", related_name='orders')

    def __str__(self):
        return f"Order No:{self.order_id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"