from django.http.response import HttpResponse, JsonResponse
from coupon_app.models import Coupon
from .serialziers import CouponSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


def coupon_list(request):
    all_coupons = Coupon.objects.all()
    my_coupon_list = []
    for coupon in all_coupons:
        coupon_dictionary = {
            "title": coupon.title,
            "expire_date": coupon.expire_date,
            "percent": coupon.percent,
            "coupon availablity": coupon.coupon_availability,
        }
        my_coupon_list.append(coupon_dictionary)

    return JsonResponse(my_coupon_list, safe=False)


class CouponView(ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["percent"]
    search_fields = ["title"]
    filterset_fields = ['percent']
    
    

class CouponDetail(RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]
    
