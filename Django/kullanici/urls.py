

from unicodedata import name
from . import views
from django.urls import path


urlpatterns = [
    path("",views.index,name="anasayfa"),
    path("index",views.index),
    path("profil",views.profil,name="profil"),
    path("update/profil/<int:id>",views.profil_update,name="profil_update"),
    path("newpassword",views.password,name="password"),
    path("password_change/<int:id>",views.password_change,name="password_change")
]