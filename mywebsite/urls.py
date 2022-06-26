
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Blog/',include('Blog.urls')),
    path('items/',include('Items.urls')),
    path('service/',include('Layanan.urls')),
    path('',views.index)
]
