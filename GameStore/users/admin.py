from django.contrib import admin
from .models import User,normalUserProfile,vipUserProfile
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



admin.site.register(User)
admin.site.register(normalUserProfile)
admin.site.register(vipUserProfile)