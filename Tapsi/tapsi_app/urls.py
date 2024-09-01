from django.urls import path
from tapsi_app.views import welcome,create_trip,trip_list, TripDetail , TripModifier , sale

urlpatterns = [
    path('' , welcome),
    path('create_trip/<str:driver_name>/<str:customer_name>/', create_trip, name='create_trip'),
    path('triplist/', trip_list, name='trip_list'),
    path('TripDetail' , TripDetail.as_view() ),
    path('TripModifier/<int:pk>' , TripModifier.as_view() ),
    path('sale/<int:inp_id>' , sale )
]