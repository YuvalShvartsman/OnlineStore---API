from django.urls import path
from .views import items_list

urlpatterns = [
    path("api/items/", items_list, name="items-list"),
]
