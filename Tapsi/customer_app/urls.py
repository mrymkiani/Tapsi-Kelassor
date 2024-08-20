from django.urls import path
from customer_app.views import customer_list, customer_list_by_trip_type

urlpatterns = [
    path("", customer_list),
    path("<str:trip_type>", customer_list_by_trip_type),
]
