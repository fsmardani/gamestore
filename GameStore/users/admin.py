from django.contrib import admin
from .models import UserProfile,SupplierProfile
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



admin.site.register(UserProfile)
admin.site.register(SupplierProfile)