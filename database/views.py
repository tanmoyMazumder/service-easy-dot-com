from django.core.checks import messages
from django.shortcuts import render
from database.models import Customer,Service
from django.contrib.auth.decorators import login_required
from .models import Customer, Payment, Service_type, ServiceProvider
import random, datetime
from database.models import Area
import sqlite3 as db
# Create your views here.

user = Customer( number = "01824637531", customer_name = "Aurnob Aurgho", email= "arnobAugrgho@gmail.com", password="vefgrege")


def newPage(request):
    phone0 = request.POST.get("customer[phone_number]")
    name0 = request.POST.get("customer[user_name]")
    email0  = request.POST.get("customer[email]")
    password0  = request.POST.get("customer[password]")

    
#    o_ref = Customer(Customer.customer_id = ID0, Customer.customer_name = name0, Customer.email= email0, Customer.password=password0)
    o_ref = Customer( number = phone0, customer_name = name0, email= email0, password=password0)
    o_ref.save()

    return render(request, 'database/login.html', {"message" : "Registration complete, log in now"})


def loginCheck(request):
    email0  = request.POST.get("customer[email]")
    password0  = request.POST.get("customer[password]")

    user_list = Customer.objects.all()
    global user
    for user0 in user_list:
        if user0.email == email0:
            if user0.password == password0:
                user = user0
                return render(request, 'database/user-profile.html', {"user" : user})
            else:
                return render(request, 'database/login.html', {"message" : "Wrong password, try again"})
        

def newPage(request):
    phone0 = request.POST.get("customer[phone_number]")
    name0 = request.POST.get("customer[user_name]")
    email0  = request.POST.get("customer[email]")
    password0  = request.POST.get("customer[password]")

    
#    o_ref = Customer(Customer.customer_id = ID0, Customer.customer_name = name0, Customer.email= email0, Customer.password=password0)
    o_ref = Customer( number = phone0, customer_name = name0, email= email0, password=password0)
    o_ref.save()

    return render(request, 'database/login.html', {"message" : "Registration complete, log in now"})
    
def bookNew(request):
    
    serviceType= request.POST.get("book[category]")
    prob= request.POST.get("book[problem]")
    add= request.POST.get("book[address]")
    ar= request.POST.get("book[area]")

    date0 =datetime.datetime.now()

    provider_list = ServiceProvider.objects.all()
    area_list = Area.objects.all()
    service_list= Service_type.objects.all()
    customer_list= Customer.objects.all()
    
    global user

    for customer in customer_list:
        if customer.email== user.email:
            cust=customer
    for service in service_list:
        if service.category== serviceType:
            serviceType=service

    for area0 in area_list:
        if area0.name == ar:
            ar=area0
            
    for provider in provider_list:
        if provider.area == ar and provider.service == serviceType.category:
            provider0 = provider
            break
        else:
            provider0=provider

    
    o_ref=Service(customer_id=cust,service=serviceType,problem=prob,address=add, service_provider = provider0,date=date0)
    o_ref.save()
    
    return render(request, 'database/book order.html', {"message" : "booking complete, chill now"})

    

def about_us(request):
    return render(request, 'database/about-us.html')

def registerProvider(request):
    return render(request, 'database/contact-us.html', {"message" : "Contact us to join as a service provider"})


def bill(request):
    service= Service.objects.all()
    payment=Payment.objects.all()
    return render(request, 'database/bill.html',{'Service':service, 'Payment':payment})

def booking(request):
    global user
    service=Service_type.objects.all()
    area = Area.objects.all()
    services= Service.objects.all()
    return render(request, 'database/book order.html',{"Service_type":service, "Area":area, "Service":services})

def contact_us(request):
    return render(request, 'database/contact-us.html')

def index(request):
    return render(request, 'database/index.html')

def login(request):
    return render(request, 'database/login.html')

def index_loggedin(request):
    global user
    return render(request, 'database/after login index.html', {"user":user})

def fourOHfour(request):
    return render(request, 'database/404.html')

def coming_soon(request):
    return render(request, 'database/coming-soon.html')


def profileInfo(request):
    global user
    service_list= Service.objects.all()

    return render(request, 'database/user-profile.html', {"user" : user,"Service":service_list})

def register(request):
    return render(request, 'database/user-register.html')

# ---------------------------------------------------------------------
# def register_submit(request):
#     name = request.POST.get("customer[user_name]")
#     mail = request.POST.get("customer[email]")
#     passw = request.POST.get("customer[password]")
#     phone = request.POST.get("customer[phone_number]")

#     obj_ref = Customer(customer_name=name, email= mail, number = phone, password = passw)
#     obj_ref.save()
#     return render(request, 'database/login.html', {"message" : "Registration complete, log in now"})
# ------------------------------------------------------





# ------------------------------------------------------------


def base(request):
    return render(request, 'database/base.html')
def test(request):
    return render(request, 'database/test.html')