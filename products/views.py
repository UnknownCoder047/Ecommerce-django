from django.shortcuts import redirect, render,HttpResponseRedirect
from products.models import Products,SizeVariant
from accounts.models import Cart,CartItem
# Create your views here.
def get_products(request,slug):
    
    
    try:
        product= Products.objects.get(slug=slug)
        context= {'product':product}
        if request.GET.get('size'):
            size= request.GET.get('size')
            quantity= request.GET.get('quantity')
            price= product.get_product_prize_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            context['quantity']=quantity
        return render(request,'products/product_view.html',context)
    
    except Exception as e:
        print(e)

def add_to_cart(request,slug):
    variant= request.GET.get('variant')
    
    user= request.user
    product=Products.objects.get(slug=slug)
    cart,_= Cart.objects.get_or_create(user= user, is_paid= False)
    cartitem= CartItem.objects.create(cart=cart,product= product,)
    if variant:
        variant=request.GET.get('variant')
        quantity= request.GET.get('quantity')
        size= SizeVariant.objects.get(size=variant)
        cartitem.size=size
        cartitem.quantity=quantity
        cartitem.save()
    
    return redirect('/')

