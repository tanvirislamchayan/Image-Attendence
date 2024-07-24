from django.shortcuts import render
from collages.models import Collage

# Create your views here.

def homa_page(request):
    collages = Collage.objects.all()


    context = {
        'page':'Home',
        'collages':collages,
    }
    return render(request, 'home/home.html', context)