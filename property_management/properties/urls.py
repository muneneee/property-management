from django.urls import path

from .views import add_property, property_list, add_house, house_list, add_tenant

urlpatterns = [
    path('add-property/', add_property, name='add_property'),
    path('property_list/', property_list, name='property_list'),
    path('add_house/<str:property_id>/', add_house, name='add_house'),
    path('property/<int:property_id>/', house_list, name='house_list'),
    path('tenant/<int:house_id>/', add_tenant, name='add_tenant'),


]