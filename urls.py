from django.urls import path, include 
from .views import * 


urlpatterns = [
  path('', include('sw_blog.api.urls')),
]
