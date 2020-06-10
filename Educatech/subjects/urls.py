from django.urls import path
from subjects.views import *


urlpatterns =[
   path('search', ProductSearchListView.as_view(), name='search'),
   path('<slug:slug>',ProductDetailView.as_view(), name='product'),
    ]
   