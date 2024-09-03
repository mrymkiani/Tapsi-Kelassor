from .models import *
from rest_framework.serializers import ModelSerializer

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"
        
