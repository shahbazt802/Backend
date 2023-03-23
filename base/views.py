from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .products import products

from .models import Product
from django.contrib.auth.models import User

from .serializers import ProductSerializers, UserSerializers, UserSerializerWithToken

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # data['username'] = self.user.username
        # data['email'] = self.user.email
        serializer = UserSerializers(self.user).data
        print("kshkd", serializer)
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    print("data", data)
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])

        )
        serializer = UserSerializerWithToken(user, many=False)
    except:
        message = "details :user with this email id already exist"
        return Response(message, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUsersProfile(request):
    user = request.user
    print("kshkd", user)
    serializers = UserSerializerWithToken(user, many=False)

    print(user)
    data = request.data
    user.first_name = data['name']
    user.email = data['email']
    user.username = data['email']
    if data['password'] != "":
        user.password = make_password(data['password'])

    user.save()

    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsersProfile(request):
    user = request.user
    print(user)
    serializers = UserSerializerWithToken(user, many=False)
    # sr = UserSerializerWithToken.get_token(user, serializers.data)
    print("sr", serializers.data['_id'])
    return Response(serializers.data)


@api_view(['GET'])
def getUsers(request):

    user = User.objects.get(id)
    print("urd", User.objects.values())

    serializers = UserSerializers(user, many=False)
    print("sdr", serializers.data)

    return Response(serializers.data)


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
