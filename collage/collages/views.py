from django.shortcuts import render, redirect
from .models import Collage
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def collage_info(request):
    return render(request, 'collage/collage.html')



def add_collage(request):



    
    return render(request, 'collage/add_collage.html')



def create_collage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        establish_date = request.POST.get('establish_date')
        category = request.POST.get('category')
        # collage_image = request.FILES.get('collage_image')
        collage_image = request.FILES.get('collage_image')
        print(collage_image)

        destrict = request.POST.get('destrict')
        post_office = request.POST.get('post_office')
        post_code = request.POST.get('post_code')
        area = request.POST.get('road')

        description = request.POST.get('description')

        collage_obj = Collage.objects.filter(code = code)
        if collage_obj.exists():
            messages.warning(request, f'Already exists!')
            return redirect('add_collage')

        if not collage_image:
            messages.warning(request, f'Please Import an image.')
            return HttpResponseRedirect(request.path_info)

        
        Collage.objects.create(
            name = name,
            code = code,
            establish_date = establish_date,
            category = category,
            area = area,
            destrict = destrict,
            post_office = post_office,
            post_code = post_code,
            description = description,
            collage_image = collage_image
        )

    return redirect('home') 

def add_image(create_obj, collage_image):
    print(create_obj)