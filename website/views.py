from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')
def contact_view(request):
    return render(request, 'website/contact.html')
def elements_view(request):
    return render(request, 'website/elements.html')


