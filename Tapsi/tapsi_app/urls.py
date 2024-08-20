from django.urls import path
from tapsi_app.views import welcome

urlpatterns = [
    path('' , welcome)
]