
from django.urls import path

from . import views

urlpatterns = [
    path("email/add", views.add_emai),
    path("email/list", views.list_email),
    path("chat", views.chat),
]
