from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField, NullBooleanField, related

# Create your models here.

Admin = (
    ('CENTRAL AUTHORITY', 'Central Authority'),
    ('MANAGER','Manager'),
    ('SERVICE PROVIDER','Service Provider')
)

Status= (
    ('D', 'D'),
    ('C', 'C')
)

Active= (
    ('Y', 'Y'),
    ('N','N')
)

# Area Table -- to identify Area---------------1
class Area(models.Model):
    name= models.CharField(max_length=60,null=True)

    def __str__(self):
        return f"{self.name}"

# Available -- Service list ---------------2
class Service_type(models.Model):
    category= models.CharField(max_length=50,unique=True,null=True)

    def __str__(self):
        return f"{self.category}"


# Admin Table--------------------3
class ServiceProvider(models.Model):
    provider_name= models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    number= models.CharField(max_length=11)
    nid=models.CharField(max_length=17, blank=True)
    area= models.ForeignKey(Area,on_delete=models.CASCADE, blank=True, related_name="user_area")
    service= models.ForeignKey(Service_type, on_delete=models.CASCADE, blank=True, related_name="Provided_Service")
    active= models.CharField(max_length=2, choices=Active, default='Y')

    def __str__(self):
        # area_id= ", ".join(str(seg) for seg in self.area_id.all())
        # area_id= ", ".join(str(seg) for seg in self.area_id.all())
        return f"{self.id} {self.area} {self.service}"


#Customer -- Details ----------------4
class Customer(models.Model):
    customer_name= models.CharField(max_length=50)
    email= models.CharField(max_length=50, unique=True)
    number= models.CharField(max_length=11)
    password= models.CharField(max_length=8)

    def __str__(self):
        return f"{self.id} {self.customer_name}"


# Service -- information table -------------------5
class Service(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="consumer", null= True, blank= True)
    service=models.ForeignKey(Service_type, on_delete=models.CASCADE, related_name="s_service", null=True)
    area= models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    problem= models.TextField(blank=True)
    address= models.TextField()
    service_provider=models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name="provider", null=True)
    date= models.DateField()
    time=models.CharField(max_length=10, blank=True)
    rate= models.FloatField(blank=True, null=True)
    review= models.CharField(max_length=300, blank=True, null=True)
    Status = models.CharField(max_length=15, choices=Status, default='D', blank=True, null= True)

    

    def __str__(self):
        return f"{self.id}-{self.customer_id}"


# Payment -- table for payment history. -------------6
class Payment(models.Model):
    receipt_number= models.ForeignKey(Service, on_delete=models.CASCADE, related_name="receipt")
    total_bill= models.IntegerField()
    provider_paid=DateField(blank=True, null=True)
    authority_paid=DateField(blank=True, null=True)
    rate= models.FloatField(blank=True, null=True)
    review= models.CharField(max_length=300, blank=True, null=True)

    

    def __str__(self):
        return f"{self.receipt_number}"


# Rating -- About Service provider -----------------7
# class Rating(models.Model):
#     receipt_number= models.ForeignKey(Service, on_delete=models.CASCADE, related_name="billNumber")
#     rate= models.IntegerField(blank=True)
#     review= models.CharField(max_length=300, blank=True)

#     def __str__(self):
#         return f"{self.receipt_number} {self.rate} {self.review}"

# merge last 2 tables.