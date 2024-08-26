from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Subjects, Semester, Probidhan
from departments.models import Departments
from .resources import SubjectResource
from tablib import Dataset
import os
from django.http import HttpResponse, Http404
from django.conf import settings

# Create your views here.

def add_subjects_demo(request):
    file_path = os.path.join(settings.BASE_DIR, 'static','demo_files', 'create-subjects.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Dsposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        
    else:
        raise Http404('File does not exist!')

def add_subjects(request):
    context = {
        'page': "Add Subjects"
    }

    if request.method == 'POST':
        new_subjects = request.FILES.get('subject_excel')

        if new_subjects:
            subject_resource = SubjectResource()
            dataset = Dataset()
            data = dataset.load(new_subjects.read(), format='xlsx')
            print(data)

            """Demo Table"""
            # Department|Semester|Probidhan|Name|Code|Theory|Practical|Credit
            # ----------|--------|---------|----|----|------|---------|------

            for row in data:
                if not row[3] or not row[4]:
                    continue
                department_obj = Departments.objects.filter(field=row[0]).first()
                semester_obj = Semester.objects.filter(name=row[1]).first()
                probidhan_obj = Probidhan.objects.filter(name=row[2]).first()

                subject_obj = Subjects.objects.filter(code=row[4],name=row[3])


                if not subject_obj:
                    subject_obj.create(
                        department = department_obj or None,
                        semester = semester_obj or None,
                        probidhan = probidhan_obj or None,
                        name = row[3],
                        code = row[4],
                        theory = row[5] or None,
                        practical = row[6] or None,
                        credits = row[7] or None
                    )
                else:continue
                

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'add_subjects_excel'))


    return render(request, 'subjects/addSubject.html', context)

def show_subjects(request):
    departments = Departments.objects.all()
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
        # department_obj = Departments.objects.get(short_name=department)

        subjects = Subjects.objects.filter(department__name=department, semester__name=semester, probidhan__name = probidhan)

        context['subjects'] = subjects
        context['selected_department'] = department
        context['selected_semester'] = semester
        context['selected_probidhan'] = probidhan



    return render(request, 'subjects/subjects.html', context)
