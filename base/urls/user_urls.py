from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # path('', views.getRoutes, name='routes'),

    path('profile/', views.getUsersProfile, name='user-profile'),
    path('profile/update', views.updateUsersProfile, name='update-profile'),
    path('register/', views.registerUser, name='register'),
    path('', views.getUsers, name='users'),
    # path('products/<str:pk>/', views.getProduct, name='product'),
    # path('products/', views.getProducts, name='products'),

]
