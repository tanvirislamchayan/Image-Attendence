from django.shortcuts import render

# Create your views here.

def show_students(request):
    return render(request, 'students/students.html')