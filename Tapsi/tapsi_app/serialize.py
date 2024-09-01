from .models import  Trip
from rest_framework.serializers import ModelSerializer

class Triperializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"
        