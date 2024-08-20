from django.contrib.admin import register, ModelAdmin

from coupon_app.models import Coupon

@register(Coupon)
class CouponAdmin(ModelAdmin):
    pass