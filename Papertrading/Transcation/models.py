# trading/models.py
from django.contrib.auth.models import User
from django.db import models
from Stocks.models import Stock
from Options.models import Option


class UserTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    transaction_type = models.CharField(max_length=10, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.stock:
            return f"{self.user.username} - {self.transaction_type} {self.quantity} shares of {self.stock.symbol}"
        elif self.option:
            return f"{self.user.username} - {self.transaction_type} {self.quantity} contracts of {self.option.symbol}"
        else:
            return "Invalid Transaction"
