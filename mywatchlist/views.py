from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    return render(request, "watchlist.html", context)

def xml(request):
    data = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json(request):
    data = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

data_watchlist_item = WatchListItem.objects.all()
context = {
    'list_watchlist':data_watchlist_item,
    'nama': 'Felix Tjahyadi',
    'student_id': '2106638614'
}
