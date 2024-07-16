from django.shortcuts import render

# Create your views here.

def show_subjects(request):
    return render(request, 'subjects/subjects.html')