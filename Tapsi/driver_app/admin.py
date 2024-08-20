from django.contrib.admin import register, ModelAdmin
from driver_app.models import Driver


@register(Driver)
class DriverAdmin(ModelAdmin):
    pass
