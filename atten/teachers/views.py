from django.shortcuts import render

# Create your views here.

# Show Teachers Info
def teachers_info(request):
    return render(request, 'teachers/teachers.html')