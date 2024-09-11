from django.http.response import HttpResponse, JsonResponse
from customer_app.models import Customer
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


def customer_list(request):
    all_customers = Customer.objects.all()
    my_customer_list = []
    for customer in all_customers:
        customer_dictionary = {
            "first name": customer.first_name,
            "last name": customer.last_name,
            "phone number": customer.phone_number,
            "source x": customer.source_x,
            "source y ": customer.source_y,
            "destiantion x": customer.destination_x,
            "destiantion y": customer.destination_y,
            "trip type": customer.trip_type,
            "availablity": customer.availability,
        }
        my_customer_list.append(customer_dictionary)

    return JsonResponse(my_customer_list, safe=False)


def customer_list_by_trip_type(request, trip_type):
    all_customers = Customer.objects.filter(trip_type=trip_type)
    my_customer_list = []
    for customer in all_customers:
        customer_dictionary = {
            "first name": customer.first_name,
            "last name": customer.last_name,
            "phone number": customer.phone_number,
            "source x": customer.source_x,
            "source y ": customer.source_y,
            "destiantion x": customer.destination_x,
            "destiantion y": customer.destination_y,
            "trip type": customer.trip_type,
            "availablity": customer.availability,
        }
        my_customer_list.append(customer_dictionary)
    return JsonResponse(my_customer_list, safe=False)



class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)
    
    
class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)
