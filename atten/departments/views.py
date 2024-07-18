from django.shortcuts import render, redirect
from django.contrib import messages
from departments.models import Departmets

# Show departments
def departments(request):
    all_departments = Departmets.objects.all()
    context = {
        'page':'Departmets',
        'departments': all_departments
    }
    return render(request, 'departments/departments.html', context = context)

# Create department
def create_dep(request):
    if request.method == 'POST':
        name = request.POST.get('department_name')

        if Departmets.objects.filter(name=name).exists():
            messages.warning(request, "Department Already exists!")
            return redirect('departments')
        else:
            Departmets.objects.create(
                name=name,
            )
            messages.success(request, "Department created successfully.")
            return redirect('departments')
    return render(request, 'departments/departments.html')



def add_img(request):
    if request.method == 'POST':
        image = request.FILES.get('department_image')
        uid = request.POST.get('department_uid')

        if not image:
            messages.warning(request, "No image choosen!")
            return redirect('departments')

        dep_obj = Departmets.objects.get(uid=uid)
        dep_obj.image = image  # Correct the typo
        dep_obj.save()
        return redirect('departments')
    return render(request, 'departments/departments.html')  # Replace 'template_name.html' with your actual template name
