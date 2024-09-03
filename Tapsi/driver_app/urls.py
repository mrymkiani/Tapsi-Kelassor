from django.urls import path
from .views import *

urlpatterns = [
    path("driver-list/", DriverView.as_view()),
    path("create-driver/", DriverView.as_view()),
    path("drivers/<int:pk>/", DriverDetail.as_view()),
]
