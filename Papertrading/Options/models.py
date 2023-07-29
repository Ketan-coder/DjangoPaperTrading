# options/models.py
from django.db import models

class Option(models.Model):
    Type = models.CharField(max_length=2, choices=[('CE', 'Call'), ('PE', 'Put')])
    strikePrice = models.IntegerField()
    expiryDate = models.DateTimeField(auto_now_add=True)
    IndexUnderlying = models.CharField(max_length=10, choices=[('NIFTY', 'NIFTY'),('BANKNIFTY', 'BANKNIFTY'),('FINNIFTY','FINNIFTY')])
    lastPrice = models.SmallIntegerField()
    # name = models.CharField(max_length=100)
    # symbol = models.CharField(max_length=10, unique=True)
    # Other option-related fields can be added here

    def __str__(self):
        return f"{self.symbol} - {self.name}"
