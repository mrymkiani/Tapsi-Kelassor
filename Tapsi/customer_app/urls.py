from django.urls import path
from customer_app.views import *

urlpatterns = [
    path("customers/", CustomerView.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path(
        "customers/trip-type/<str:trip_type>/",
        customer_list_by_trip_type,
        name="customer-list-by-trip-type",
    ),
    path('create-customer/' , CustomerView.as_view()),
]
