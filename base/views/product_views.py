from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from base.products import products

from base.models import Product


from base.serializers import ProductSerializers, UserSerializers, UserSerializerWithToken

# Create your views here.


from rest_framework import status


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductSerializers(products, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializers(product, many=False)

    # product = None
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    return Response(serializer.data)
