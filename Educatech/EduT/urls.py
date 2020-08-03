from django.contrib import admin
from django.urls import path, include
from educatech.views import *
from users.views import *
from subjects.views import *
from categories.views import *

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [

    path('', ProductListView.as_view(), name='index'),
    path('edu/', include('educatech.urls')),
    path('categorias/', include('categories.urls')),
    path('admin/', admin.site.urls),
    path('productos/', include('subjects.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
    path('pagos/', include('billing_profiles.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)