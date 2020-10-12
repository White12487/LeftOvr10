from django.shortcuts import render

def home(request):
    return render(request, 'Homepage.html')

def cust(request):
    return render(request, 'CustomerRegisteration.html')

def rest(request):
    return render(request, 'RestaurantRegisteration.html')

def land(request):
    return render(request, 'LandingPage.html')

def abou(request):
    return render(request, 'AboutUs.html')
