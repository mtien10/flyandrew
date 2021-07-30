from django.urls import path
from blog.apps.views import index

urlpatterns = [
    path('', index, name='home'),
]