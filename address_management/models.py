from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    
    class Meta:
        db_table = "country_management"

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    country = models.ForeignKey(to=Country,on_delete=models.PROTECT)

    class Meta:
        db_table = "state_management"

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    state = models.ForeignKey(to=State,on_delete=models.PROTECT)

    class Meta:
        db_table = "city_management"

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    city = models.ForeignKey(to=City,on_delete=models.PROTECT)
    scraped_id = models.IntegerField()

    class Meta:
        db_table = "area_management"

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    area = models.ForeignKey(to=Area,on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = "building_management"

class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    building = models.ForeignKey(to=Building,on_delete=models.PROTECT)

    class Meta:
        db_table = "floor_management"

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    floor = models.ForeignKey(to=Floor,on_delete=models.PROTECT)

    class Meta:
        db_table = "room_management"