from django.shortcuts import render

# Create your views here.

def homa_page(request):
    context = {
        'page':'Image Polytechninc Institute'
    }
    return render(request, 'home/home.html', context)