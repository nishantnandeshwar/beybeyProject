from django.db import models

class DischargeBridgeMinuteData(models.Model):
    timestamp = models.DateTimeField()
    record = models.IntegerField()
    battv_avg = models.CharField(max_length=255)
    system_temp_avg = models.CharField(max_length=255)
    temp_c_avg = models.CharField(max_length=255)
    water_velocity = models.CharField(max_length=255)
    water_column = models.CharField(max_length=255)
    signal_quality = models.CharField(max_length=255)
    water_discharge = models.CharField(max_length=255)
