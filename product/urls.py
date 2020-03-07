from django.urls import path 
from .views import * 

urlpatterns = [
    path('',all,name="product-home"),
    path('create/',create,name="product-create"),
    path('edit/',edit,name="product-edit"),
    path('delete/',delete,name="product-delete"),
]