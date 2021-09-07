from django.contrib import admin
from .models import normalUserProfile,vipUserProfile
# Register your models here.
admin.site.register(normalUserProfile)
admin.site.register(vipUserProfile)