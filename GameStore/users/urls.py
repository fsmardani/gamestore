from django.contrib import admin
from django.urls import path
from .views import login_view,logout_view,email_activate,signup,phone_register,dashboard,supplier_register




urlpatterns = [
    path('register/', signup, name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('activate/<str:uidb64>/<str:token>', email_activate, name='activate'),
    path('phone_register/',phone_register,name='phone_register'),
    path('supplier_register/',supplier_register,name='supplier_register'),


]