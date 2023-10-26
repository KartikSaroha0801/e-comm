from django.urls import path
from . import logview
from product import views

urlpatterns = [
    path("", logview.login),
    path("", views.index),

]

