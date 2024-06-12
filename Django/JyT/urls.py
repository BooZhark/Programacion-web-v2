from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("", views.contacto, name="contacto"),
    path("", views.login, name="login"),
    path("", views.monitores, name="monitores"),
    path("", views.registro, name="registro"),
    path("", views.sbnosotros, name="sbnosotros"),
    path("", views.tarjvideo, name="tarjvideo"),
    path("", views.user_add, name="user_add"),
]