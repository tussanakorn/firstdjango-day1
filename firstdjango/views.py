from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Welcome to Django")


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About Us")


def search(request, keyword, page):
    return HttpResponse(f'Search for: {keyword} Page: {page}')


def maps(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.7245601')
    lon = request.GET.get('lon', '100.4930241')
    zoom = request.GET.get('z', 11)

    return HttpResponse(f"Map type: {type} <br> \
        Location: {lat},{lon}<br> \
        Zoom: {zoom}")