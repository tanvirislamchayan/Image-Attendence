from django.shortcuts import render, redirect
from datetime import timedelta
from departments.models import Departmets
from subjects.models import Subjects, Semester, Probidhan
from teachers.models import TeacherProfile
from .models import StudentShift, Student

# Create your views here.

def show_students(request):


    if not request.user.is_authenticated:
        context = {
            'page': 'Unable to Access.'
        }
        return render(request, 'base/not_to_access.html', context=context)
    
    departments = Departmets.objects.all()
    semesters = Semester.objects.all()
    teachers = TeacherProfile.objects.filter(is_active=True)
    shifts = StudentShift.objects.all()

    context = {
        'page': 'Students Info.',
        'departments':departments,
        'semesters':semesters,
        'teachers':teachers,
        'shifts':shifts,
    }

    if request.user.teacherProfile and request.user.teacherProfile.is_active == True:
        selected_teacher = request.user.username
        selected_department = request.user.teacherProfile.department.name
        print(selected_department)

        context['selcted_teacher'] = selected_teacher
        context['selected_department'] = selected_department
    
    if request.method == 'POST':
        date = request.POST.get('date')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        shift = request.POST.get('shift')

        students = Student.objects.filter(department__name=department, semester__name = semester, shift__shift = shift)
        subjects = Subjects.objects.filter(department__name=department, semester__name = semester)

        context['selcted_semester'] = semester
        context['selected_department'] = department
        context['selected_date'] = date
        context['selected_shift'] = shift
        context['students'] = students
        context['subjects'] = subjects
        
    return render(request, 'students/students.html', context=context)


def add_dates(request):


    context = {}
    return redirect('students')

   
        # current_date = start_date
        # invoices_by_date = {}

        # while current_date <= end_date:
        #     invoices = self.env['account.move'].search([
        #         ('invoice_date', '=', current_date),
        #         ('journal_id.type', '=', 'sale')
        #     ])

        #     if invoices:
        #         invoices_by_date[current_date] = []

        #         for invoice in invoices:
        #             invoices_by_date[current_date].append(invoice.amount_total)

        #     current_date += datetime.timedelta(days=1)