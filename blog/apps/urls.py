from django.urls import path
from blog.apps.views import *

urlpatterns = [
    path('', index, name='home'),
    path('page2', page2),
]