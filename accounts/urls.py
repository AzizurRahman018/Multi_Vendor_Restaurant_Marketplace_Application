
from django.urls import path

from accounts import views



urlpatterns = [
    path('registerUser/',views.registerUser,name="registerUser"),
    path('registervendor/',views.registerVendor,name="registerVendor")
]