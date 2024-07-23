from django.shortcuts import render

# Create your views here.


def collage_info(request):
    return render(request, 'collage/collage.html')



def add_collage(request):
    return render(request, 'collage/add_collage.html')