from django.shortcuts import render
from .models import Subjects, Semester, Probidhan
from departments.models import Departmets

# Create your views here.

def show_subjects(request):
    departments = Departmets.objects.all()
    semesters = Semester.objects.all()
    subjects = Subjects.objects.all()
    probidhans = Probidhan.objects.all()

    print(departments)
    
    # print(request.user.teacherProfile)

    context = {
        'page':'Subjects',
        'departments':departments,
        'semesters':semesters,
        'probidhans':probidhans,
    }

    if request.method == 'POST':
        semester = request.POST.get('semester')
        department = request.POST.get('department')
        probidhan  = request.POST.get('probidhan')

        # semseter_obj = Semester.objects.get(name=semester)
        # department_obj = Departmets.objects.get(short_name=department)

        subjects = Subjects.objects.filter(department__name=department, semester__name=semester, probidhan__name = probidhan)

        context['subjects'] = subjects
        context['selected_department'] = department
        context['selected_semester'] = semester
        context['selected_probidhan'] = probidhan



    return render(request, 'subjects/subjects.html', context)
