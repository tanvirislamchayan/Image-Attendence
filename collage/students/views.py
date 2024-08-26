from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta
from departments.models import Departments
from subjects.models import Subjects, Semester, Probidhan
from teachers.models import TeacherProfile
from .models import StudentShift, Student, GenDate, Attendence
from django.contrib import messages
from datetime import datetime,timedelta
import datetime
from collages.models import Collage
from .resources import StudentResource
from tablib import Dataset
import os
from django.http import HttpResponse, Http404
from django.conf import settings

# Create your views here.

def download_demo_excel(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'demo_files', 'create-student.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("File does not exist")




"""create students with excel"""
def add_students(request):
    context = {
        'page': 'Add Student'
    }
    if request.method == 'POST':
        # Safely retrieve the uploaded file, if any
        new_student = request.FILES.get('student_excel')

        if new_student:
            student_resource = StudentResource()
            dataset = Dataset()
            data = dataset.load(new_student.read(), format='xlsx')

            """ example Table"""

            #  Collage Code|Student Name|SR no|Roll|Registration|Seasson|Semester|Department- Field|Probidhan|Shift
            #  ------------|------------|-----|----|------------|-------|--------|-----------------|---------|-----

            for row in data:
                if not row[1]:
                    continue

                collage_obj = Collage.objects.filter(code=row[0]).first() 
                semester_obj = Semester.objects.filter(name=row[6]).first() 
                department_obj = Departments.objects.filter(field=row[7]).first() 
                probidhan_obj = Probidhan.objects.filter(name=row[8]).first()
                shift_obj = StudentShift.objects.filter(shift=row[9]).first()

                student_obj = Student.objects.filter(collage=collage_obj, roll=row[3], registration=row[4])
                if not student_obj:
                    student_obj.create(
                        collage=collage_obj,
                        name=row[1],
                        sr_no=row[2],
                        roll=row[3],
                        registration=row[4],
                        seasson=row[5],
                        semester=semester_obj if semester_obj else None,
                        department=department_obj if department_obj else None,
                        probidhan=probidhan_obj if probidhan_obj else None,
                        shift=shift_obj if shift_obj else None
                    )
                else:continue
        referer_url = request.META.get('HTTP_REFERER', 'add_student')  # Fallback to 'delete' if no referer
        return HttpResponseRedirect(referer_url)

    return render(request, 'students/addStudent.html', context)






def show_students(request):
    user_obj = request.user
    teacher_obj = TeacherProfile.objects.get(teacher=user_obj)
    dates = GenDate.objects.filter(teacher=teacher_obj)
    collage_objs = Collage.objects.all()
    teacher_collage_obj = teacher_obj.collage
    department_objs = Departments.objects.all()
    teacher_department_obj = teacher_obj.department
    probidhan_objs = Probidhan.objects.all()
    semester_objs = Semester.objects.all()
    group_objs = StudentShift.objects.all()
    print(user_obj)

    context = {
        'page': "Student Attendence",
        'selected_teacher':teacher_obj,
        'dates':dates,
        'collages':collage_objs,
        'teacher_collage':teacher_collage_obj,
        'departments':department_objs,
        'selected_department':teacher_department_obj,
        'probidhans':probidhan_objs,
        'semesters':semester_objs,
        'shifts':group_objs
    }

    # Date section
    start_date = ''
    end_date = ''
    selected_collage = ''
    selected_department = ''
    selected_probidhan = ''
    selected_semester = ''
    selected_group = ''
    subjects_objs = ''
    student_objs = ''
    group = ''
    if 'fromDate' in request.GET:
        start_date = request.GET.get('fromDate')
        context['start_date'] = start_date
    if 'toDate' in request.GET:
        end_date = request.GET.get('toDate')
        context['end_date'] = end_date
    if start_date and end_date:
        gen_date(start_date, end_date, teacher_obj)
    
    # collage
    if 'collage' in request.GET:
        collage = request.GET.get('collage')
        selected_collage = Collage.objects.get(slug=collage)
        context['selected_collage'] = selected_collage
    # department
    if 'department' in request.GET:
        department = request.GET.get('department')
        selected_department = Departments.objects.get(slug=department)
        context['selected_department']=selected_department
    # Probidhan
    if 'probidhan' in request.GET:
        probidhan = request.GET.get('probidhan')
        selected_probidhan = Probidhan.objects.get(name=probidhan)
        context['selected_probidhan']=selected_probidhan
    # semester
    if 'semester' in request.GET:
        semester = request.GET.get('semester')
        selected_semester = Semester.objects.get(name=semester)
        context['selected_semester']=selected_semester
    # group
    if 'group' in request.GET:
        group = request.GET.get('group')
        if group != 'any':
            selected_group = StudentShift.objects.get(shift=group)
        context['selected_group']=selected_group
    print(group)

    # subjects
    if selected_department and selected_probidhan and selected_semester:
        subjects_objs = Subjects.objects.filter(department=selected_department, probidhan=selected_probidhan, semester=selected_semester)
        context['subjects']=subjects_objs
   
    if group == 'any' and selected_collage and selected_department and selected_semester and selected_probidhan:
        student_objs = Student.objects.filter(
                collage=selected_collage,
                department=selected_department,
                semester=selected_semester,
                probidhan = selected_probidhan,
            )
    if group != 'any' and selected_collage and selected_department and selected_semester and selected_probidhan and selected_group:
        student_objs = Student.objects.filter(
                collage=selected_collage,
                department=selected_department,
                semester=selected_semester,
                probidhan = selected_probidhan,
                shift = selected_group
            )

    context.update({
        'students':student_objs
    })

    
    # POST
    if request.method == 'POST':
        present_subject = request.POST.get('present_subject')
        present_date = request.POST.get('present_date')
        present_students = request.POST.getlist('present')


    




    # print(context)
    return render(request, 'students/students.html', context=context)


def gen_date(from_date, to_date, teacher_obj):
    date_obj = GenDate.objects.filter(teacher=teacher_obj)
    date_obj.delete()
    current_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')

    while current_date <= end_date:
        GenDate.objects.create(
            teacher=teacher_obj,
            date=current_date
        )
        current_date += timedelta(days=1)



def add_dates(request):


    context = {}
    return redirect('attendence')
