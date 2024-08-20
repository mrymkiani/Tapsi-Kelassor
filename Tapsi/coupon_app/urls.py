from django.urls import path
from coupon_app.views import coupon_list

urlpatterns = [
    path('' , coupon_list)
]