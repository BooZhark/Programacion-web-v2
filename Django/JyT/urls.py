from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contacto", views.contacto, name="contacto"),
    path("login", views.login, name="login"),
    path("monitores", views.monitores, name="monitores"),
    path("registro", views.registro, name="registro"),
    path("sbnosotros", views.sbnosotros, name="sbnosotros"),
    path("tarvideo", views.tarjvideo, name="tarjvideo"),
    path("crud", views.crud, name="crud"),
    path("user_add", views.user_add, name="user_add"),
    path("user_del/<str:pk>", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("user_update", views.user_update, name="user_update"),
]