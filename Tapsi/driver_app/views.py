from django.http.response import HttpResponse, JsonResponse
from driver_app.models import Driver
from .serialziers import DriverSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


def driver_list(request):
    all_drivers = Driver.objects.all()
    my_driver_list = []
    for driver in all_drivers:
        driver_dictionary = {
            "first name": driver.first_name,
            "last name": driver.last_name,
            "phone number ": driver.phone_number,
            "car model": driver.car_model,
            "car plate": driver.car_plate,
            "car color": driver.car_color,
            "wallet": driver.wallet,
        }
        my_driver_list.append(driver_dictionary)
    return JsonResponse(my_driver_list, safe=False)


class DriverView(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Driver.objects.filter(user=self.request.user)


class DriverDetail(RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Driver.objects.filter(user=self.request.user)
