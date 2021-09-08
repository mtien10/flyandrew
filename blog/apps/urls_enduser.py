from django.urls import path
from .view_enduser import *

urlpatterns = [
    path('', index),
    path('view-product/<pk>', view_product),
    path('order-product/<pk>', order_product),
    path('thank-you', thank_you),
]