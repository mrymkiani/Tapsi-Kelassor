from django.http.response import HttpResponse, JsonResponse
from coupon_app.models import Coupon


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

    return JsonResponse(my_coupon_list,safe=False)