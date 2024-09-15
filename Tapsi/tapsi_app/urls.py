from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('trips/', TripDetail.as_view(), name='trip-list'),
    path('trips/<int:pk>/', TripModifier.as_view(), name='trip-detail'),
    path('createtrip/<str:driver_name>/<str:customer_name>/', create_trip, name='create-trip'),
    path('sale/<int:inp_id>/', sale, name='sale'),
    path('login/', Login.as_view(), name='token_obtain_pair'),
    path('login/refresh/', Refresh.as_view(), name='token_refresh'),
    path('create-trip/' , TripDetail.as_view()),
    path('rate-trip/<int:trip_id>/', rate_trip),
    path('find-path/' , api_to_neshan)
]
