from django.urls import path
from subjects.views import *


urlpatterns =[
   path('', ProductListView.as_view(), name='index'),
    ]
   