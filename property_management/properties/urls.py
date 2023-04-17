from django.urls import path

from .views import add_property, property_list

urlpatterns = [
    path('add-property/', add_property, name='add_property'),
    path('property_list/', property_list, name='property_list'),

]