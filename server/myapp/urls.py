from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),
    path("fullprizes/", views.get_allPrizes, name="all_prizes"),
    path("fulllaureate/", views.get_allLaureate, name="all_laureate"),
    path("fullcountriescode/", views.get_allCountries, name="all_countries_code")
    ]