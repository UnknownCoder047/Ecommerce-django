from django.shortcuts import render
import razorpay
# Create your views here.
def payment(request):
    product= request.GET.get('product')
    selection= request.GET.get('type')
    amt= request.GET.get('amt')
    context= {'product':product}
    context['type']= selection
    context['amt']=amt
    return render(request,'payment/payment.html',context)

def payment_done(request):
    selection= request.GET.get('type')
    if request.GET.get('type')== 'buy_now':
        product= request.GET.get('product')
    return render(request,'accounts/orders.html')