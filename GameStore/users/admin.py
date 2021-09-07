from django.contrib import admin
from .models import User,normalUserProfile,vipUserProfile
# Register your models here.
admin.site.register(User)
admin.site.register(normalUserProfile)
admin.site.register(vipUserProfile)