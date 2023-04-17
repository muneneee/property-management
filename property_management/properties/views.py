from django.shortcuts import render, redirect
from .models import Property, House, Tenant, Invoice, Receipt


def add_property(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        client_details = request.POST['client_details']
        property_address = request.POST['property_address']
        # Create property object and save to the database
        property = Property(property_id=property_id, client_details=client_details, property_address=property_address)
        property.save()
        return redirect('/view_properties')
    return render(request, 'add_property.html')