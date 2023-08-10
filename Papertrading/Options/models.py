# options/models.py
from django.db import models
from Stocks.models import Stock
from Commodity.models import Commodity
from Crypto.models import Crypto
from .CustomExceptions import MultipleFieldsFilledError

class Option(models.Model):
    Type = models.CharField(max_length=2, choices=[('CE', 'Call'), ('PE', 'Put')])
    strikePrice = models.IntegerField()
    expiryDate = models.DateField()
    lotSize = models.IntegerField(default=1)
    stockUnderlying = models.OneToOneField(Stock, on_delete=models.CASCADE, null=True, blank=True)
    CommodityUnderlying = models.OneToOneField(Commodity, on_delete=models.CASCADE, null=True, blank=True)
    CryptoUnderlying = models.OneToOneField(Crypto, on_delete=models.CASCADE, null=True, blank=True)
    IndexUnderlying = models.CharField(max_length=10, null=True, blank=True, choices=[('NIFTY', 'NIFTY'),('BANKNIFTY', 'BANKNIFTY'),('FINNIFTY','FINNIFTY')])
    lastPrice = models.FloatField(default=0)

    def clean(self):
        filled_fields = []
        for field in [self.stockUnderlying, self.CommodityUnderlying, self.IndexUnderlying, self.CryptoUnderlying]:
            if field:
                filled_fields.append(field)
        
        if len(filled_fields) != 1:
            raise MultipleFieldsFilledError(["stockUnderlying", "CommodityUnderlying", "IndexUnderlying","CryptoUnderlying"])
        else:
            return True
        
    def __str__(self):
        if self.clean() != True:
            pass
        else:
            if self.stockUnderlying != None:
                return f"{self.stockUnderlying.symbol} - {self.Type} - Strike Price: {self.strikePrice} - {self.expiryDate}"
            elif self.CommodityUnderlying != None:
                return f"{self.CommodityUnderlying.symbol} - {self.Type} - Strike Price: {self.strikePrice} - {self.expiryDate}"
            elif self.IndexUnderlying != None:
                return f"{self.IndexUnderlying} - {self.Type} - Strike Price: {self.strikePrice} - {self.expiryDate}"
            elif self.CryptoUnderlying != None:
                return f"{self.CryptoUnderlying.symbol} - {self.Type} - Strike Price: {self.strikePrice} - {self.expiryDate}"
            else:
                return f"{self.Type} - Strike Price: {self.strikePrice} - {self.expiryDate}"
    
    def CalculatePrice(self):
        return self.lastPrice * self.lotSize