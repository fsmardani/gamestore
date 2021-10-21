
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .views import index, header, footer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
 #   path('',header,name='header'),
 #   path('',footer,name='footer'),
    path('',include('users.urls')),
    path('',include('product.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
