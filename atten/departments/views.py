from django.shortcuts import render

# Create your views here.


# show departments
def departmets(request):
    return render(request, 'departments/departments.html')