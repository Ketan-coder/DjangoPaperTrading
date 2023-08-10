from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from .models import Stock

def update_stock_data(request):
    symbols = ['TATASTEEL.NS','RVNL.NS','RELIANCE.NS','TCS.NS']  # Add stock symbols you want to track
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        # print(data)
        lastPrice = data['Close'].iloc[-1]
        Stock.objects.update_or_create(symbol=symbol, defaults={'lastPrice': lastPrice, 'name': symbol[:-3]})
    return JsonResponse({'message': 'Stock data updated successfully'})


def live_stock_data(request):
    stocks = Stock.objects.all()
    return render(request, 'live_stock.html', {'stocks': stocks})
