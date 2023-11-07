from django.urls import path
from accounts.views import *
from products.views import add_to_cart
urlpatterns = [
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('add-to-cart/<slug>/',add_to_cart,name='add_to_cart'),
    path('cart/',cart,name='cart'),
    path('remove-item/<uid>/',remove_item,name='remove_item'),
    path('buy-now/<slug>/',buy_now,name='buy_now'),
    path('profile/',get_profile,name='profile'),
    path('create-profile/<user>/',create_profile,name='create_profile'),
    path('orders/',orders,name='orders'),
    path('logout/',logout_page,name='logout')
]
