from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", include("tapsi_app.urls")),
    path('customerlist/' , include('customer_app.urls')),
    path('customerlisttype/' , include('customer_app.urls')),
    path('driverlist/' , include('driver_app.urls')),
    path('couponlist/' , include('coupon_app.urls')),
    path('tapsi/', include('tapsi_app.urls')),
]
