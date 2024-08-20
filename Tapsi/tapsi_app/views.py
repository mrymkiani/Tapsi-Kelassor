from django.http.response import HttpResponse, JsonResponse
from tapsi_app.models import Trip
from driver_app.models import Driver
from customer_app.models import Customer
import math


def welcome(request):
    return HttpResponse("Welcome to Tapsi")


def find_driver(request, driver_name):
    driver = Driver.objects.get(first_name=driver_name)
    return driver


def find_customer(request, customer_name):
    customer = Customer.objects.get(first_name=customer_name)
    return customer


def calculate_trip_cost(request, customer_name):
    customer = find_customer(request , customer_name)
    return abs((customer.source_x + customer.source_y) - (customer.destination_x + customer.destination_y)) * 10000


def add_driver_wallet(request, driver_name , customer_name):
    driver = find_driver(request, driver_name)
    driver.trip_cost = calculate_trip_cost(request , customer_name)
    driver.wallet = driver.wallet + calculate_trip_cost(request , customer_name)
    return HttpResponse(driver.trip_cost)