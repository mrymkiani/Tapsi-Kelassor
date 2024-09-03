from django.http.response import HttpResponse, JsonResponse
from coupon_app.models import Coupon
from .serialziers import CouponSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


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
    
    

class CouponDetail(RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]
    
