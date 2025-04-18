# Generated by Django 5.2 on 2025-04-18 14:56

import api.product.utilities
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234567890', db_index=True, length=4, max_length=4, prefix='', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234567890', db_index=True, length=8, max_length=10, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.product.utilities.product_image_upload)),
            ],
        ),
    ]
