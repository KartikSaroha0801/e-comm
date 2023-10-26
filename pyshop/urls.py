from django.contrib import admin
from django.urls import path, include
from . import mainview

urlpatterns = [
    path("", mainview.index),
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
    path("product/", include("product.urls")),
    path("login/", include("login.urls"))
]
