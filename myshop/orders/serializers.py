from rest_framework import serializers
from .models import Order, OrderItem
from shop.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_name', 'price', 'quantity', 'get_cost']


class OrderSerializer(serializers.ModelSerializer):
    item = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'address', 'postal_code', 'city',
            'created', 'updated', 'paid', 'stripe_id',
            'item', 'get_total_cost'
        ]
