from django.contrib import admin
from .models import Property, House, Tenant, Invoice, Receipt


admin.site.register(Property)
admin.site.register(House)
admin.site.register(Tenant)
