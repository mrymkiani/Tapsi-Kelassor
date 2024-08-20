from django.urls import path
from driver_app.views import welcome, driver_list

urlpatterns = [path("", welcome), path("driverlist", driver_list)]
