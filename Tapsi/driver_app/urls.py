from django.urls import path
from driver_app.views import  driver_list

urlpatterns = [path("", driver_list)]
