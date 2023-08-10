from django.urls import path
from .views import update_stock_data, live_stock_data

urlpatterns = [
    path('update_stock/', update_stock_data, name='update_stock'),
    path('live_stock_data/', live_stock_data, name='live_stock_data'),
]
