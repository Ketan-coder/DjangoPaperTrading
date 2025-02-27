# OptionChainViewer/views.py

from django.http import JsonResponse
from nsetools import Nse
from django.shortcuts import render

def option_chain_data(request):
    nse = Nse()
    symbol = 'RELIANCE'  # Replace with the desired stock symbol

    option_chain_data = nse.get_option_chain(symbol)
    if option_chain_data:
        data = option_chain_data['records']['data']
        return render(request, 'optionchainviewer/option_chain_table.html', {'data': data})
    else:
        return JsonResponse({'error': 'Data not available'})
