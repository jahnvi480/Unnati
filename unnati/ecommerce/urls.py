from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="ShopHome"),
    path('cart',views.cart, name="ShopCart"),
    path('checkout',views.checkout,name="checkout"),
    path('login',views.login,name="login"),
    path("logout", views.account_logout, name="UNNATI | Logout"),
    path("product_<int:myid>",views.product,name="UNNATI | Product_Info"),
    path('register',views.register,name="register"),
]