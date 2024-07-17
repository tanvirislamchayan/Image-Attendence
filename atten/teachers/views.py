from django.shortcuts import render, redirect, get_object_or_404
from departments.models import Departmets
from . models import TeacherProfile
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# Show Teachers Info
def teachers_info(request):
    departments = Departmets.objects.all()
    teachers = TeacherProfile.objects.filter(is_active=True)
    context = {
        'page':'Teachers',
        'departments':departments,
        'teachers':teachers
    }
    return render(request, 'teachers/teachers.html', context=context)


def add_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        department = request.POST.get('department')
        designation = request.POST.get('designation')
        hiest_digree = request.POST.get('hiest_digree')
        versity = request.POST.get('versity')



        get_user_obj = User.objects.filter(username = email)
        if get_user_obj.exists():
            messages.warning(request, "User already exists!")
            return redirect('teachers')
        
        
        if not get_user_obj:
            user_obj = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = email,
            )
            user_obj.set_password(password)
            department_obg = Departmets.objects.get(short_name=department)
            TeacherProfile.objects.create(
                teacher = user_obj,
                department = department_obg,
                designation = designation,
                hiest_digree = hiest_digree,
                versity = versity,
            )

            
    return redirect('teachers')


def teacher_detail(request, uid):
    teacher = TeacherProfile.objects.get(uid=uid)
    print
    page = f'{teacher.teacher.first_name} {teacher.teacher.last_name}'
    context = {
        'page': page,
        'teacher':teacher
    }
    return render(request, 'teachers/teahcer_detail.html', context=context )

def upload_profile(request):
    if request.method == 'POST':
        img = request.FILES.get('profileImage')  
        uid = request.POST.get('uid')

        if not img:
            return redirect('teachers_detail', uid=uid)
        if img:
            teacher_obj = get_object_or_404(TeacherProfile, uid=uid)
            teacher_obj.teacher_image = img
            teacher_obj.save()


    return redirect('teachers_detail', uid=uid)


def upload_routine(request):
    if request.method == 'POST':
        img = request.FILES.get('routine_img') 
        uid = request.POST.get('uid')

        if not img:
            return redirect('teachers_detail', uid=uid)

        teacher_obj = get_object_or_404(TeacherProfile, uid=uid)

        teacher_obj.routine_img = img
        teacher_obj.save()


    return redirect('teachers_detail', uid=uid)

# Login
def user_login(request):
    return render(request, 'teachers/login.html')