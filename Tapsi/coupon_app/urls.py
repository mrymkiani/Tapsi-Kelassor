from django.urls import path
from .views import *

urlpatterns = [
    path('couponlist/' , coupon_list),
    path('coupon-list/' , CouponView.as_view()),
    path('create-coupon/' , CouponView.as_view()),
]