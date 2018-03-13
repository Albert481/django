from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=60, default='null')
    ethaddress = models.CharField(max_length=20, default='null')
    indicativecontribution = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    actualcontribution = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    mytoken = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    bonustoken = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    tokenwithdrawn = models.DecimalField(max_digits=5, default=0, decimal_places=2)