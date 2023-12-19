from django.db import models
from client_management.models import VendorDetails, CustomerDetails, DepartmentDetails
import uuid


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "category_management"

    def __str__(self):
        return f"{self.name}"


class PurchasedBillingDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vendor = models.ForeignKey(to=VendorDetails, on_delete=models.PROTECT)
    amount = models.FloatField()
    # products = models.ManyToManyField(to=Category)
    sgst = models.FloatField()
    cgst = models.FloatField()
    is_verified = models.BooleanField()
    description = models.CharField(max_length=128)

    class Meta:
        db_table = "purchased_billing_details"


class SoldBillingDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(to=CustomerDetails, on_delete=models.PROTECT)
    amount = models.FloatField()
    # products = models.ManyToManyField(to=Category)
    sgst = models.FloatField()
    cgst = models.FloatField()
    is_verified = models.BooleanField()
    description = models.CharField(max_length=128)

    class Meta:
        db_table = "sold_billing_details"


class PurchasedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(to=VendorDetails, on_delete=models.PROTECT)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.FloatField(max_length=100, blank=True, null=True)
    # bill = models.ForeignKey(to=SoldBillingDetails,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "purchased_product_management"


class SoldProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(to=CustomerDetails, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(max_length=100, blank=True, null=True)
    # bill = models.ForeignKey(to=SoldBillingDetails,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sold_product_management"

    def __str__(self):
        return f"Customer {self.customer} on {self.created_at}"


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    catergory = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "inventory_management"


class InHouseProducts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        to=DepartmentDetails, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "inhouse_product_management"

    def __str__(self):
        return self.name
