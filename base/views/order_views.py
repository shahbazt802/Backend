from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from base.products import products

from base.models import Product, Order, OrderItem, ShippingAddress


from base.serializers import ProductSerializers, UserSerializers, UserSerializerWithToken, OrderSerializers
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'details': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            totalPrice=data['totalPrice']


        )
        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country']



        )

        for i in orderItems:
            product = Product.objects.get(_id=i['product'])
            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=i['name'],
                qty=i['qty'],
                # image=product.image.url

            )
            product.countInStock -= item.qty
            product.save()

        serializers = OrderSerializers(order, many=False)

        return Response(serializers.data)
