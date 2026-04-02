from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Welcome to GOgreen App 🌱")

# def about(request):
#     return HttpResponse("GOgreen is about protecting environment")

def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def service(request):
    return render(request, 'service.html')

def gallery(request):
    return render(request, 'gallery.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def donation(request):
    return render(request, 'donation.html')

def contact(request):
    return render(request, 'contact.html')

def causes(request):
    return render(request, 'causes.html')

def about(request):
    return render(request, 'about.html')

def four_oh_four(request):
    return render(request, '404.html')

def blog(request):
    return render(request, 'blog.html')

def base(request):
    return render(request, 'base.html')