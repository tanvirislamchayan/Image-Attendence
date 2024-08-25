from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from departments.models import Departments
from collages.models import Collage

# Show departments
def departments(request):
    collages = Collage.objects.all()
    all_departments = Departments.objects.all()
    context = {
        'page':'Departments',
        'departments': all_departments,
        'collages':collages
    }
    return render(request, 'departments/departments.html', context = context)

# Create department
def create_dep(request):
    if request.method == 'POST':
        name = request.POST.get('department_name')
        collage = request.POST.get('department_name')
        field = request.POST.get('department_field')

        collage_obj = Collage.objects.filter(slug = collage).filter()

        if Departments.objects.filter(name=name).exists():
            messages.warning(request, "Department Already exists!")
            return redirect('departments')
        else:
            Departments.objects.create(
                collage = collage_obj if collage_obj else None,
                name=name,
                field = field
                
            )
            messages.success(request, "Department created successfully.")
            return redirect('departments')
    return render(request, 'departments/departments.html')



def add_img(request):
    if request.method == 'POST':
        image = request.FILES.get('department_image')
        uid = request.POST.get('department_uid')
        print(image)

        if not image:
            messages.warning(request, "No image choosen!")
            return redirect('departments')

        dep_obj = Departments.objects.get(uid=uid)
        dep_obj.image = image  # Correct the typo
        dep_obj.save()
        return redirect('departments')
    return render(request, 'departments/departments.html')  # Replace 'template_name.html' with your actual template name
