

from django.urls import path
from base.views import product_views as views


urlpatterns = [
    # path('users/login/', views.MyTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('', views.getRoutes, name='routes'),

    # path('users/profile/', views.getUsersProfile, name='user-profile'),
    # path('users/profile/update', views.updateUsersProfile, name='update-profile'),
    # path('users/register/', views.registerUser, name='register'),
    # path('users/', views.getUsers, name='users'),
    path('<str:pk>/', views.getProduct, name='product'),
    path('', views.getProducts, name='products'),

]
