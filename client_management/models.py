from django.db import models
from django.contrib.auth.models import User


class PartnerDetails(models.Model):
    id = models.AutoField(primary_key=True)
    partner = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True, unique=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.FileField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "partner_management"

class ClientDetails(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=50, unique=True)
    partner = models.ForeignKey(PartnerDetails, on_delete=models.PROTECT, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=128, blank=True, null=True, unique=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.FileField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "client_management"

class VendorDetails(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=128, blank=True, null=True, unique=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.FileField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = "vendor_management"

    def __str__(self):
        return f"{self.vendor}"


class CustomerDetails(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=128, blank=True, null=True, unique=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.FileField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "customer_management"

    def __str__(self):
        return f"{self.customer}"


class DepartmentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)
    user = models.ForeignKey(to=User,on_delete=models.PROTECT)
    description = models.CharField(max_length=128)

    class Meta:
        db_table = "department_management"