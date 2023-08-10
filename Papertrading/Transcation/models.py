# trading/models.py
from django.contrib.auth.models import User
from django.db import models
from Stocks.models import Stock
from Options.models import Option
from Options.CustomExceptions import MultipleFieldsFilledError
from Crypto.models import Crypto
from Commodity.models import Commodity
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver


class UserTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, null=True, blank=True)
    cryto = models.ForeignKey(Crypto, on_delete=models.CASCADE, null=True, blank=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    transaction_type = models.CharField(max_length=10, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        filled_fields = []
        for field in [self.stock, self.commodity, self.option, self.cryto]:
            if field:
                filled_fields.append(field)
        
        if len(filled_fields) != 1:
            raise MultipleFieldsFilledError(["stock", "commodity", "option", "crypto"])
        else:
            return True

    def __str__(self):
        if self.clean() != True:
            pass
        else:
            if self.stock != None:
                return f"{self.user.username} - {self.transaction_type} {self.quantity} shares of {self.stock.symbol}"
            elif self.commodity != None:
                return f"{self.user.username} - {self.transaction_type} {self.quantity} commodities of {self.commodity.symbol}"
            elif self.cryto != None:
                return f"{self.user.username} - {self.transaction_type} {self.quantity} cryptos of {self.cryto.symbol}"
            elif self.option != None:
                return f"{self.user.username} - {self.transaction_type} {self.quantity} contracts of {self.option}"
            else:
                return f"{self.user.username} - {self.transaction_type} {self.quantity}"

@receiver(post_save, sender=UserTransaction)
def UpdatingPricePerUnit(sender, created, instance, **kwargs):
    if created:
        if instance.clean() != True:
            pass
        else:
            if instance.stock != None:
                instance.price_per_unit = instance.quantity * instance.stock.lastPrice
            elif instance.option != None:
                instance.price_per_unit = instance.quantity * instance.option.lastPrice
            elif instance.cryto != None:
                instance.price_per_unit = instance.quantity * instance.cryto.lastPrice
            elif instance.commodity != None:
                instance.price_per_unit = instance.quantity * instance.commodity.lastPrice
            else:
                instance.price_per_unit = instance.quantity * 1
        instance.save()