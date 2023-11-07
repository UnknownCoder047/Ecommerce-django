from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.dispatch import receiver
from products.models import *
# Create your models here.

class Profile(BaseModel):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=50)
    profile_image= models.ImageField(upload_to='profile')
    address= models.TextField(max_length=200)
    mobile_no= models.CharField(max_length=10 )
    def get_cart_count(self):
        return CartItem.objects.filter(cart__is_paid=False, cart__user= self.user).count()
    
    def __str__(self):
        return self.email_token
    

class Cart(BaseModel):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    is_paid= models.BooleanField(default=False)

class CartItem(BaseModel):
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product= models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True )
    #color= models.ForeignKey(ColorVariant,on_delete=models.SET_NULL,null=True,blank=True )
    size= models.ForeignKey(SizeVariant,on_delete=models.SET_NULL,null=True,blank=True )
    quantity= models.CharField(max_length=10,default='1')
    
    def get_product_price(self):
        price=[self.product.price]
        
        if self.size:
            size_price= self.size.price
            price.append(size_price)
        
        return sum(price)