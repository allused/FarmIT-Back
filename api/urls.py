from django.urls import path
from . import views


urlpatterns = [
    path("farms/", views.FarmListCreate.as_view(), name="farm"),
    path("farms/types", views.FarmTypeList.as_view(), name="farm-types"),
    path("farms/delete/<int:pk>", views.FarmDelete.as_view(), name="delete-farm")
]
