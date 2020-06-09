from django.urls import path
from educatech.views import *


urlpatterns =[
    path('usuarios/login/', login_view, name='login'),
    path('usuarios/logout/', logout_view, name='logout'),
    path('usuarios/registro/', register, name='register'),
]