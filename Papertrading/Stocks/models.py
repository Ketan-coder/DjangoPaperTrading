# stocks/models.py
from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50, unique=True)
    lastPrice = models.IntegerField()

    def __str__(self):
        return f"{self.symbol} - {self.name} - {self.lastPrice}"
