from django.urls import path, include
from demodayapp.views import index , sac , price

urlpatterns = [
    path('', index),
    path('sac', sac),
    path('price', price)
   
]
