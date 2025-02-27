from django.urls import path
from .views import option_chain_data

urlpatterns = [
    # path('option_chain/', option_chain_view, name='option_chain'),
    path('option_chain_data/', option_chain_data, name='option_chain_data'),
]
