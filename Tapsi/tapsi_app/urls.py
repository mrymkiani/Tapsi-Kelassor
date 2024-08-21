from django.urls import path
from tapsi_app.views import welcome,create_trip,trip_list

urlpatterns = [
    path('' , welcome),
    path('create_trip/<str:driver_name>/<str:customer_name>/', create_trip, name='create_trip'),
    path('triplist/', trip_list, name='trip_list'),
]