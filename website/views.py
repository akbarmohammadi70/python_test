from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse("<h1>This is http Home_page</h1>")

def about_view(request):
    return HttpResponse("<h1>This is http about_view</h1>")
def contact_view(request):
    return HttpResponse("<h1>This is http contact_view</h1>")


