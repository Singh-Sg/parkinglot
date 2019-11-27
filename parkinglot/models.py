from django.db import models


class ParkingSlot(models.Model):
	"""
	ParkingSlot Where creating Slot with car informations
	"""
    car_color = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=30)
    slot_number = models.IntegerField(max_length=30)