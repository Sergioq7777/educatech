from django.contrib import admin
from django.urls import path, include
from educatech.views import *
from users.views import *
from subjects.views import *
from categories.views import *
from chat.views import *

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('messages/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('edu/', include('educatech.urls')),
    path('', ProductListView.as_view(), name='index'),
    path('productos/', include('subjects.urls')),
    path('categorias/', include('categories.urls')),
    
    #path('users/', include('users.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)