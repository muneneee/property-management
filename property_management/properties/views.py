from django.shortcuts import render, redirect
from .models import Property, House, Tenant, Invoice, Receipt
from .forms import TenantForm, HouseForm, PropertyForm, InvoiceForm


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def add_house(request, property_id):
    property = Property.objects.get(property_id=property_id)
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.property = property
            house.save()
            return redirect('house_list', property_id=property_id)
    else:
        form = HouseForm()
    return render(request, 'add_house.html', {'form': form, 'property': property})

def house_list(request, property_id):
    houses = House.objects.filter(property__property_id=property_id)
    property = Property.objects.get(property_id=property_id)
    return render(request, 'house_list.html', {'houses': houses, 'property': property})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            #  invoice for the tenant
            rent = 200  # Fixed rent amount
            garbage_service = 200  # Fixed garbage service amount
            invoice = Invoice(tenant=tenant, rent=rent, garbage_service=garbage_service)
            invoice.save()           
            return redirect('property_list')
    else:
        form = TenantForm()
        invoice_form = InvoiceForm()

    return render(request, 'add_tenant.html', {'form': form, 'invoice_form': invoice_form})

def invoice_detail(request, invoice_id):
    invoice = Invoice.objects.get(invoice_id=invoice_id)
    return render(request, 'invoice_detail.html', {'invoice': invoice})