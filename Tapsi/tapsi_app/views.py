from django.http import JsonResponse, HttpResponse
from tapsi_app.models import Trip
from driver_app.models import Driver
from customer_app.models import Customer
from coupon_app.models import Coupon
import json
from datetime import date
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialize import Triperializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView , token_refresh


def welcome(request):
    return HttpResponse("Welcome to Tapsi")


def create_trip(request, driver_name, customer_name):
    if request.method == "GET":
        try:
            driver = Driver.objects.get(first_name=driver_name)
            customer = Customer.objects.get(first_name=customer_name)

            base_trip_cost = (
                abs(
                    (customer.source_x + customer.source_y)
                    - (customer.destination_x + customer.destination_y)
                )
                * 10000
            )
            if base_trip_cost == 0:
                base_trip_cost = 100000

            coupon = customer.coupons
            if (
                coupon
                and coupon.coupon_availability
                and coupon.expire_date >= date.today()
            ):
                discount = base_trip_cost * (coupon.percent / 100)
                trip_cost = base_trip_cost - discount
            else:
                trip_cost = base_trip_cost
                coupon = None

            trip = Trip.objects.create(
                driver=driver,
                customer=customer,
                coupon=coupon,
                payment_status=False,
                trip_cost=trip_cost,
            )

            driver.wallet += trip_cost
            driver.save()

            if coupon:
                coupon.coupon_availability = False
                coupon.save()

            return JsonResponse({"status": "success", "trip_id": trip.trip_id})
        except Driver.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Driver not found"}, status=404
            )
        except Customer.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Customer not found"}, status=404
            )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=405
    )


def trip_list(request):
    trips = Trip.objects.all()
    trip_data = []

    for trip in trips:
        trip_data.append(
            {
                "trip_id": trip.trip_id,
                "driver": trip.driver.first_name,
                "customer": trip.customer.first_name,
                "trip_cost": trip.trip_cost,
                "payment_status": trip.payment_status,
                "coupon": (trip.coupon.title if trip.coupon else None),
            }
        )

    return JsonResponse(trip_data, safe=False)


class TripDetail(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = Triperializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)

class TripModifier(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = Triperializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)