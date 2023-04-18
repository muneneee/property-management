from django.shortcuts import render, redirect
from .models import Property, House, Tenant, Invoice, Receipt


def add_property(request):
    if request.method == 'POST':
        
        client_details = request.POST['client_details']
        property_address = request.POST['property_address']
        # Create property object and save to the database
        property = Property(client_details=client_details, property_address=property_address)
        property.save()
        return redirect('/view_properties')
    return render(request, 'add_property.html')


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def add_house(request, property_id):
    property = Property.objects.get(property_id=property_id)
    if request.method == 'POST':
        # Get data from form
        house_rent = request.POST.get('house_rent')
        deposit = request.POST.get('deposit')
        
        # Create House object and save to database
        house = House(property=property, house_rent=house_rent, deposit=deposit)
        house.save()
        
        return redirect('/view_properties')
    return render(request, 'add_house.html', {'property': property})

def house_list(request, property_id):
    houses = House.objects.filter(property__property_id=property_id)
    property = Property.objects.get(property_id=property_id)
    return render(request, 'house_list.html', {'houses': houses, 'property': property})