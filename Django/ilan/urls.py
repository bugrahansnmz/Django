
from . import views
from django.urls import path


urlpatterns = [
    path("add_advert",views.add_advert,name="add_advert"),
    path("search_advert",views.search_advert,name="search_advert")
]