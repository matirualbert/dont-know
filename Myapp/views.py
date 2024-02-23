from django.shortcuts import render

def home(request):
    return render(request, 'index.html'),
def about(request):
    return render(request, 'about.html'),
def book(request):
    return render(request, 'booking.html'),
def contact(request):
    return render(request, 'contact.html'),
def menu(request):
    return render(request, 'menu.html'),
def team(request):
    return render(request, 'team.html'),
def service(request):
    return render(request, 'service.html'),
def testimonials(request):
    return render(request, 'testimonial.html'),


# Create your views here.
