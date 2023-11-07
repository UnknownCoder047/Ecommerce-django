from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from products.models import Products, SizeVariant
from .models import Profile,Cart,CartItem
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user_obj= User.objects.filter(username=username)
        if not user_obj.exists():
            messages.warning(request,'Account not found!')
            return HttpResponseRedirect(request.path_info)
        
        user_obj=authenticate(username=username,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        
    return render(request,'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def register_page(request):
    if request.method=='POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        
        
        user_obj= User.objects.filter(username= email)
        if user_obj.exists():
            messages.warning(request,'Email already exits!')
            return HttpResponseRedirect(request.path_info)
        
        user_obj= User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,'Account created successfully')
        if user_obj:
            login(request,user_obj)
        return redirect('create_profile',user= user_obj.username)
    
    return render(request,'accounts/register.html')

def remove_item(request,uid):
    try:
        item= CartItem.objects.get(uid=uid)
        item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_cart_total(cart_items):
        price= []
        for cart_item in cart_items:
            quantity= int(cart_item.quantity)
            if quantity > 1:
                price.append((cart_item.product.price * quantity))
            else:
                price.append(cart_item.product.price)
            if cart_item.size:
                price.append(cart_item.size.price)
        print(price)
        return sum(price)

def get_discount(total_price):
    if total_price>=1000 and total_price<3000:
        discount=100
    elif total_price >= 3000 and total_price < 5000:
        discount=500
    elif total_price>=5000:
        discount=800
    else:
        discount=0
    return discount

def cart(request):
    user= request.user
    cart= Cart.objects.get(user=user)
    cartitem= CartItem.objects.filter(cart=cart)
    total=get_cart_total(cartitem)
    discount=get_discount(total)
    final_price= total - discount
    context= {'cartitem':cartitem,'get_total':total,'get_discount':discount,'final_price':final_price}
    return render(request,'accounts/cart.html',context)

def buy_now(request,slug):
    variant= request.GET.get('variant')
    product=Products.objects.get(slug=slug)
    context={'product':product}
    if variant:
        variant=request.GET.get('variant')
        quantity= int(request.GET.get('quantity'))
        size= SizeVariant.objects.get(size=variant)
    
    price=[]
    if quantity>1:
        price.append((product.price * quantity))
    else:
        price.append(product.price)
    if size:
        price.append(size.price)
    
    total= sum(price)
    discount= get_discount(total)
    final_amt= total- discount
    
    context['quantity']= quantity
    context['size']=size
    context['discount']= discount
    context['total']=total
    context['final_price']= final_amt
    return render(request,'accounts/buy_now.html',context)

def get_profile(request):
    
    user= request.user
    profile= Profile.objects.get(user=user)
    context={'profile':profile}
    
    return render(request,'accounts/profile.html',context)

def create_profile(request,user):
    if request.method=='POST':
        mobile_no= request.POST.get('mobile_no')
        address= request.POST.get('address')
        profile_image= request.FILES.get('profile_image')
        user_obj= User.objects.get(username=user)
        profile= Profile.objects.create(user= user_obj, mobile_no= mobile_no, address= address,profile_image=profile_image,email_token=user)
        profile.save()
        return redirect('/')
        
    return render(request,'accounts/create_profile.html')

def orders(request):
    return render(request,'accounts/orders.html')