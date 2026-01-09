from django.shortcuts import render
from django.http import HttpResponse    
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def bootstrap_template(request):
    return render(request, 'template_bootstrap.html')

def bootsraptemplate_index(request):
    return render(request, 'bootsraptemplate_index.html')

def data_diri(request):
    return render(request, 'data_diri.html')

def index_page(request):
    return render(request, 'index_page.html')

def main_page(request):
    return render(request, 'main_page.html')
# Data Diri Website Views
def datadiri_home(request):
    return render(request, 'datadiri_home.html')

def about_me(request):
    return render(request, 'about_me.html')

def gallery(request):
    return render(request, 'gallery.html')