from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
class ProductImageAdmin(admin.StackedInline):
    model= ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','category','price']
    inlines=[ProductImageAdmin]

class ColorVariantAdmin(admin.ModelAdmin):
    list_display=['color','price']
    model= ColorVariant

class SizeVariantAdmin(admin.ModelAdmin):
    list_display=['size','price']
    model= SizeVariant

admin.site.register(SizeVariant,SizeVariantAdmin)
admin.site.register(ColorVariant,ColorVariantAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(ProductImage)