from django.urls import path

from . import views


urlpatterns = [
    path('',views.MyLayanan.as_view(),name="service")
]