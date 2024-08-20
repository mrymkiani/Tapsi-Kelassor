from django.contrib.admin import register, ModelAdmin
from customer_app.models import Customer


@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass
