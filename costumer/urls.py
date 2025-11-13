from  django.urls import path
from .views import viewList

urlpatterns = [
    path("costumer/", viewList, name="lists")
]
