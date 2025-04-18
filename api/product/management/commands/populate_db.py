import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from api.product.models import Product, Order, OrderItem
from api.user.models import User


class Command(BaseCommand):
    help = "Creates application data"

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username="admin").first()
        if not user:
            user = User.objects.create_superuser(username="admin", password="test")

        # create products - name, desc, price, stock, image
        products = [
            Product(
                name="A Scanner Darkly",
                info=lorem_ipsum.paragraph(),
                price=Decimal("12.99"),
                quantity=4,
            ),
            Product(
                name="Coffee Machine",
                info=lorem_ipsum.paragraph(),
                price=Decimal("70.99"),
                quantity=6,
            ),
            Product(
                name="Velvet Underground & Nico",
                info=lorem_ipsum.paragraph(),
                price=Decimal("15.99"),
                quantity=11,
            ),
            Product(
                name="Enter the Wu-Tang (36 Chambers)",
                info=lorem_ipsum.paragraph(),
                price=Decimal("17.99"),
                quantity=2,
            ),
            Product(
                name="Digital Camera",
                info=lorem_ipsum.paragraph(),
                price=Decimal("350.99"),
                quantity=4,
            ),
            Product(
                name="Watch",
                info=lorem_ipsum.paragraph(),
                price=Decimal("500.05"),
                quantity=0,
            ),
        ]

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()

        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1, 3)
                )
