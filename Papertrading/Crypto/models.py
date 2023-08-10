from django.db import models

# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    lastPrice = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.symbol} - Last Price: {self.lastPrice}"