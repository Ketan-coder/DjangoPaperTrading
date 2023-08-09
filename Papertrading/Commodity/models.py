from django.db import models

# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    lastPrice = models.IntegerField()
    # Other stock-related fields can be added here

    def __str__(self):
        return f"{self.symbol} - {self.name} - {self.lastPrice}"