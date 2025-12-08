from rest_framework import serializers
from .models import Client, Password, Order, OrderItem, Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'count']  # name и price заполняются автоматически

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'total', 'created_at', 'status', 'address', 'items']
        read_only_fields = ['total', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        # вытаскиваем адрес, если он пришёл
        address = validated_data.get('address')

        order = Order.objects.create(
            client=validated_data['client'],
            address=address
        )

        total = 0
        for item_data in items_data:
            product = item_data['product']
            count = item_data['count']
            price = product.price
            total += price * count

            OrderItem.objects.create(
                order=order,
                product=product,
                name=product.name,
                count=count,
                price=price
            )

        order.total = total
        order.save()
        return order

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
