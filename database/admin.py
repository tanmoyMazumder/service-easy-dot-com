from django.contrib import admin
from database.models import ServiceProvider, Area, Customer, Payment, Service, Service_type 


# # #Area
# class area(admin.ModelAdmin):
#     list_display = ("id","area_id", "area_name")

# #Service_type
# class srvt(admin.ModelAdmin):
#     list_display = ("id","service_id", "service_name")

class admin_table(admin.ModelAdmin):
    list_display = ("id","provider_name","email","number","nid","area","service","active")

#Customer
class client(admin.ModelAdmin):
    list_display = ("customer_name", "email", "number", "password")

# #Service
class srv(admin.ModelAdmin):
    list_display = ("id","customer_id", "service", "area", "problem", "address", "service_provider_id", "date", "time","rate","review", "Status")

# #Rating
class rate(admin.ModelAdmin):
    list_display = ("receipt_number", "rate", "review")

# #Payment 
class payment(admin.ModelAdmin):
    list_display= ("id","receipt_number", "total_bill", "provider_paid", "authority_paid")


# # Register your models here.

admin.site.register(Area)
admin.site.register(Service_type)
admin.site.register(ServiceProvider,admin_table)
admin.site.register(Customer,client)
admin.site.register(Service,srv)
# admin.site.register(Rating,rate)
admin.site.register(Payment,payment)
#admin.site.register(Payment,payment)

