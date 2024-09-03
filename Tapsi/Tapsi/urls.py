from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", include("tapsi_app.urls")),
    path('customer/' , include('customer_app.urls')),
    path('driver/' , include('driver_app.urls')),
    path('coupon/' , include('coupon_app.urls')),
    path('tapsi/', include('tapsi_app.urls')),
]
