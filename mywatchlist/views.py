from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = WatchList.objects.all()

    message = ""
    udhnonton = 0
    blmnonton = 0
    
    for film in data_mywatchlist:
        if film.watched == True:
            udhnonton+=1
        else :
            blmnonton+=1

    if(udhnonton >= blmnonton):
        message = ("Selamat, kamu sudah banyak menonton!")
    else:
        message = ("Wah, kamu masih sedikit menonton!")

    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Rakhan Yusuf Rivesa',
        'npm': '2106751852',
        'message': message
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_xml = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json(request):
    data_json = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_json_by_id(request, id):
    data_json_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json_id), content_type="application/json")

def show_xml_by_id(request, id):
    data_xml_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_xml_id), content_type="application/xml")