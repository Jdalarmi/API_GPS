from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=30)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()

class Position(models.Model):
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()