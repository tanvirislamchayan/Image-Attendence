from django.shortcuts import render, redirect
from datetime import timedelta
from departments.models import Departments
from subjects.models import Subjects, Semester, Probidhan
from teachers.models import TeacherProfile
from .models import StudentShift, Student
from django.contrib import messages

# Create your views here.

def filter_data(request, context):
    print(context)


def show_students(request):


    if not request.user.is_authenticated:
        context = {
            'page': 'Unable to Access.'
        }
        messages.warning(request, f"May be you're not allowd access this page. Please contract with the administrator!")
        return render(request, 'base/not_to_access.html', context=context)
    
    departments = Departments.objects.all()
    semesters = Semester.objects.all()
    teachers = TeacherProfile.objects.filter(is_active=True)
    shifts = StudentShift.objects.all()
    probidhans = Probidhan.objects.all()

    context = {
        'page': 'Students Info.',
        'departments':departments,
        'semesters':semesters,
        'teachers':teachers,
        'shifts':shifts,
        'probidhans':probidhans,
    }

    if request.user.teacherProfile and request.user.teacherProfile.is_active == True:
        selected_teacher = request.user.username
        selected_department = request.user.teacherProfile.department.name if request.user.teacherProfile.department else False

        context['selected_teacher'] = selected_teacher
        context['selected_department'] = selected_department
    
    if request.method == 'POST':

        # Filter Students
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        shift = request.POST.get('shift')
        probidhan = request.POST.get('probidhan')

        # Present Students
        p_date = request.POST.get('date')
        p_department = request.POST.get('p_department')
        p_semester = request.POST.get('p_semester')
        p_probidhan = request.POST.get('p_probidhan')
        p_shift = request.POST.get('p_shift')
        p_teacher = request.POST.get('p_teacher')
        p_subject = request.POST.get('p_subject')
        present = request.POST.get('present')
        print(present)

        s_department = p_department if p_department else department
        s_semester = p_semester if p_semester else semester
        s_shift = p_shift if p_shift else shift
        s_probidhan = p_probidhan if p_probidhan else probidhan


        students = Student.objects.filter(department__name=s_department, semester__name = s_semester, shift__shift = s_shift, probidhan__name = s_probidhan)
        subjects = Subjects.objects.filter(department__name=s_department, semester__name = s_semester, probidhan__name = s_probidhan)



        # if not s_shift:
        #     students = Student.objects.filter(department__name=s_department, semester__name = s_semester)

        # if not probidhan:
        #     students = Student.objects.filter(department__name=s_department, semester__name = s_semester)
        #     subjects = Subjects.objects.filter(department__name=s_department, semester__name = s_semester)

        context['selected_department'] = s_department
        context['selcted_semester'] = s_semester
        context['selected_shift'] = s_shift
        context['selected_probidhan'] = s_probidhan
        context['selected_teacher'] =request.user.username if not p_teacher else p_teacher
        context['selected_subject'] =p_subject

        context['students'] = students
        context['subjects'] = subjects





        context['selected_date'] = p_date


    return render(request, 'students/students.html', context=context)





def add_dates(request):


    context = {}
    return redirect('attendence')

   
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