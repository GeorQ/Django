from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
import csv, codecs


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    file = settings.BUS_STATION_CSV
    cont = []
    with open(file, encoding="cp1251", errors='ignore') as source_file:
        reader = csv.DictReader(source_file, delimiter=",")
        header = next(reader)
        for row in reader:
            dict = {'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
                    }
            cont.append(dict)

    paginator = Paginator(cont, 15, 3)
    current_page = int(request.GET.get('page', 1))
    articles = paginator.get_page(current_page)
    if articles.has_next():
        next_page_url = articles.next_page_number
    return render_to_response('index.html', context={
        'bus_stations': articles,
        'current_page': articles.number,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })
