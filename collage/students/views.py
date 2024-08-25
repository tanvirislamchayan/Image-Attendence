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


# Create your views here.




def show_students(request):
    if not request.user.is_authenticated:
        context = {'page': 'Unable to Access.'}
        messages.warning(request, "You may not be allowed to access this page. Please contact the administrator!")
        return render(request, 'base/not_to_access.html', context=context)

    context = {
        'page': 'Students Info.',
        'semesters': Semester.objects.all(),
        'shifts': StudentShift.objects.all(),
        'probidhans': Probidhan.objects.all(),
        'collages': Collage.objects.all()
    }


    teacher_profile = getattr(request.user, 'teacherProfile', None)
    if teacher_profile and teacher_profile.is_active:
        selected_teacher = teacher_profile
        selected_department_slug = selected_teacher.department.slug if selected_teacher.department else None
        selected_collage = selected_teacher.collage
        today_date = datetime.date.today()
        last_attendance = Attendence.objects.filter(teacher=selected_teacher, created_at__date=today_date).order_by('-created_at').first()
        dates_obj = GenDate.objects.filter(teacher=selected_teacher)

        context.update({
            'selected_teacher': selected_teacher,
            'selected_department': selected_department_slug,
            'selected_collage': selected_collage,
            'teacher_collage': selected_teacher.collage,
            'dates' : [date_obj.date.strftime('%Y-%m-%d') for date_obj in dates_obj],
        })

        if last_attendance:
            context.update({
                'selected_date': last_attendance.date.strftime('%Y-%m-%d'),
                'selected_probidhan': last_attendance.probidhan.name,
                'selected_shift': last_attendance.group.shift if last_attendance.group else None,
                'selected_semester': last_attendance.semester.name,
                'selected_subject': last_attendance.subject.slug,
                'last_attends': last_attendance.present_students.all()
            })
    else:
        messages.warning(request, "You're not allowed! Your ID has been deactivated. Please contact the administrator.")
        return render(request, 'base/not_to_access.html', {'page': "Not allowed!"})

    if 'toDate' in request.GET:
        context['todate'] = request.GET.get('toDate')

    if 'fromDate' in request.GET:
        context['fromDate'] = request.GET.get('fromDate')

    if 'fromDate' in request.GET and 'toDate' in request.GET:
        from_date = request.GET.get('fromDate')
        to_date = request.GET.get('toDate')

        if from_date and to_date:
            if from_date > to_date:
                messages.warning(request, 'From date must be smaller than To date!')
                return HttpResponseRedirect(request.path_info)
            gen_date(from_date, to_date, selected_teacher)

    # if selected_teacher is not None:
           

    requested_collage = request.GET.get('collage', '')
    requested_department = request.GET.get('department', '')
    requested_semester = request.GET.get('semester', '')
    requested_probidhan = request.GET.get('probidhan', '')
    requested_shift = request.GET.get('group', '')

    if requested_collage:
        if not request.user.is_superuser and selected_teacher.collage.slug != requested_collage:
            messages.warning(request, "You are not allowed to access the documents of this collage. Please contact the Administrator!")
            return render(request, "base/not_to_access.html")

        context['selected_collage'] = requested_collage
        context['departments'] = Departments.objects.filter(collage__slug=requested_collage)

    if requested_department:
        context['selected_department'] = requested_department

    if requested_semester:
        context['selected_semester'] = requested_semester

    if requested_probidhan:
        context['selected_probidhan'] = requested_probidhan

    if requested_department and requested_semester and requested_probidhan:
        context['subjects'] = Subjects.objects.filter(department__slug=requested_department, semester__name=requested_semester, probidhan__name=requested_probidhan)

    if requested_collage and requested_department and requested_probidhan and requested_semester and requested_shift:
        if requested_shift == 'any':
            students = Student.objects.filter(collage__slug=requested_collage, department__slug=requested_department, semester__name=requested_semester).order_by('sr_no')
        else:
            students = Student.objects.filter(collage__slug=requested_collage, department__slug=requested_department, semester__name=requested_semester, shift__shift=requested_shift).order_by('sr_no')

        context['students'] = students

    if request.method == 'POST':
        present_date = request.POST.get('present_date')
        present_subject = request.POST.get('present_subject')

        collage_obj = Collage.objects.filter(slug=requested_collage).first()
        department_obj = Departments.objects.filter(slug=requested_department, collage__slug=requested_collage).first()
        probidhan_obj = Probidhan.objects.filter(name=requested_probidhan).first()
        semester_obj = Semester.objects.filter(name=requested_semester).first()
        group_obj = StudentShift.objects.filter(shift=requested_shift).first()
        subject_obj = Subjects.objects.filter(slug=present_subject, department=department_obj).first()

        applied_students = request.POST.getlist('present')
        present_students = [student for student in students if str(student.uid) in applied_students]
        absent_students = [student for student in students if str(student.uid) not in applied_students]

        get_attendance = Attendence.objects.filter(
            collage=collage_obj,
            department=department_obj,
            probidhan=probidhan_obj,
            semester=semester_obj,
            group=group_obj,
            date=present_date,
            subject=subject_obj
        )

        if get_attendance.exists():
            messages.warning(request, 'Already presented. Please contact the administrator!')
            return render(request, 'base/not_to_access.html')
        else:
            attendance = Attendence.objects.create(
                collage=collage_obj,
                department=department_obj,
                probidhan=probidhan_obj,
                semester=semester_obj,
                group=group_obj,
                date=present_date,
                subject=subject_obj,
                teacher=selected_teacher
            )

            attendance.present_students.set(present_students)
            attendance.absent_students.set(absent_students)
            attendance.save()
            return HttpResponseRedirect(request.path_info)

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
