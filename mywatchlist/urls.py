import imp
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import xml
from mywatchlist.views import json
app_name = 'mywatchlist'

urlpatterns = [
    path('html', show_watchlist, name='show_watchlist'),
    path('xml', xml, name='xml'),
    path('json', json, name='json'),
]
