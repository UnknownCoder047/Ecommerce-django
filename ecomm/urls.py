from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from payment.views import payment,payment_done
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('home.urls')),
    path('products/',include('products.urls')),
    path('payment/',payment,name='payment'),
    path('paymentdone/',payment_done,name='paymentdone')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()

