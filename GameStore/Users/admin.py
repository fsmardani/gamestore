from django.contrib import admin
# Register your models here.
from GameStore.Users.models import CustomUserManager, Normal_user, Vip_user

admin.site.register(CustomUserManager)
admin.site.register(Normal_user)
admin.site.register(Vip_user)