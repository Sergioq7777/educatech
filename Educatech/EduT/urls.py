from django.contrib import admin
from django.urls import path, include
from educatech.views import *
from users.views import *
from subjects.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('', include('educatech.urls')),
    path('', include('subjects.urls')),

]
