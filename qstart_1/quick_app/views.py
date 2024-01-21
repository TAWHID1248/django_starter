from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'quick_app/home.html')