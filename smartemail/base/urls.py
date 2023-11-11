
from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
    path("status", views.status),
]
