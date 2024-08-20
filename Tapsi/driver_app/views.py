from django.http.response import HttpResponse, JsonResponse
from driver_app.models import Driver

def welcome(request):
    return HttpResponse("Welcome to Tapsi")

def driver_list(request):
    all_drivers = Driver.objects.all()
    my_driver_list = []
    for driver in all_drivers:
        driver_dictionary = {
            "first name" : driver.first_name,
            "last name" : driver.last_name,
            "phone number " : driver.phone_number,
            "car model" : driver.car_model,
            "car plate" : driver.car_plate,
            "car color" : driver.car_color,
            "wallet" : driver.wallet
        }
        my_driver_list.append(driver_dictionary)
    return JsonResponse(my_driver_list , safe=False)
        