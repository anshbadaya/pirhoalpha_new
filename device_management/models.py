from django.db import models



class Device(models.Model):

    PARAMETERS_CHOICES = [
    ('pm25', 'PM25'),
    ('pm10', 'PM10'),
    ('pm1', 'PM1'),
    ('no2', 'NO2'),
    ('so2', 'SO2'),
    ('o2', 'O2'),
    ('o3', 'O3'),
    ('nh3', 'NH3'),
    ('temp', 'TEMP'),
    ('hum', 'HUM'),
    ('tvoc', 'TVOC'),
    ('co2', 'CO2'),
    ('sound', 'SOUND'),
                        ]
    
    device_id = models.CharField(max_length=128)
    node_addr = models.CharField(max_length=128)
    condition = models.CharField(max_length=128)

    def __str__(self):
        return f"Device {self.device_id}"
    
    class Meta:
        db_table = "devices"
