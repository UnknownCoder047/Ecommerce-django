from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.


class Category(BaseModel):
    category_name= models.CharField(max_length=100)
    slug= models.SlugField(unique=True,null=True,blank=True)
    category_image= models.ImageField(upload_to="categories")
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name

class ColorVariant(BaseModel):
    color=models.CharField(max_length=100)
    price= models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.color

class SizeVariant(BaseModel):
    size=models.CharField(max_length=100)
    price= models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.size

class Products(BaseModel):
    product_name= models.CharField(max_length=100)
    slug= models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price=models.IntegerField(default=0)
    product_description=models.TextField()
    color= models.ManyToManyField(ColorVariant,blank=True)
    size= models.ManyToManyField(SizeVariant,blank=True)
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super(Products,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name

    def get_product_prize_by_size(self,size):
        return self.price + SizeVariant.objects.get(size= size).price


class ProductImage(BaseModel):
    product= models.ForeignKey(Products,on_delete=models.CASCADE,related_name='product_images')
    image=models.ImageField(upload_to='product')

