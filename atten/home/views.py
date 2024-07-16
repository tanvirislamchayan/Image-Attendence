from django.shortcuts import render

# Create your views here.

def homa_page(request):
    return render(request, 'home/home.html')