from django.shortcuts import render, redirect, get_object_or_404
from departments.models import Departments
from collages.models import Collage
from . models import TeacherProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# Show Teachers Info
def teachers_info(request):
    departments = Departments.objects.all()
    teachers = TeacherProfile.objects.filter(is_active=True)

    if 'teacher' in request.GET:
        uid = request.GET.get('teacher')
        teacher_obj = TeacherProfile.objects.get(uid=uid)

        page = f'{teacher_obj.teacher.first_name} {teacher_obj.teacher.last_name}'


        context = {
            'page':page,
            'teacher':teacher_obj
        }

        return render(request, 'teachers/teahcer_detail.html', context=context)

    context = {
        'page':'Teachers',
        'departments':departments,
        'teachers':teachers
    }
    return render(request, 'teachers/teachers.html', context=context)


def add_teacher(request):
    collages = Collage.objects.all()
    departments = Departments.objects.all()

    context = {
        'page':'Add Teacher',
        'collages':collages,
        # 'departments':departments,
    }

    if 'collage' in request.GET:
        collage = request.GET.get('collage')
        departments = Departments.objects.filter(collage__slug = collage)
        context['collage_slug'] = collage
        context['departments'] = departments
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        image = request.FILES.get('teacher_image')
        hiest_digree = request.POST.get('hiest_digree')
        versity = request.POST.get('versity')
        # collage = request.POST.get('collage')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')

        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        user_esxists = User.objects.filter(username=email)
        if user_esxists.exists():
            messages.warning(request, 'User already exists!')
            return HttpResponseRedirect(request.path_info)
        
        if password != confirm_pass:
            messages.warning(request, "Password doesn't match!")

            context = {
                'page':'Add Teacher',
                'collages':collages,
                'departments':departments,

                'first_name':first_name,
                'last_name':last_name,
                'hiest_digree':hiest_digree,
                'versity':versity,
                'collage_slug':collage,
                'department_name':department,
                'designation':designation,
                'email':email,
                'phone':phone,
                'password':password,
            }
            return render(request, 'teachers/add_teacher.html', context=context)
            

        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email,
        )

        user_obj.set_password(password)
        user_obj.save()

        collage_obj = Collage.objects.filter(slug = collage).first()
        print(collage_obj)

        department_obj = Departments.objects.filter(name=department).first()
        print(department_obj)

        TeacherProfile.objects.create(
            teacher = user_obj,
            collage = collage_obj,
            department = department_obj,
            designation = designation,
            hiest_digree = hiest_digree,
            versity = versity,
            phone = phone,
            teacher_image = image
        )


        
    return render(request, 'teachers/add_teacher.html', context=context)


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
        print(img)
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
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Get user
        try:
            user_obj = User.objects.get(username=email)
        except User.DoesNotExist:
            messages.warning(request, 'Invalid Username')
            return HttpResponseRedirect(request.path_info)

        # Check if the user's teacher profile is active, except for superusers
        if not user_obj.is_superuser:
            teacher_profile = TeacherProfile.objects.filter(teacher__username=email, is_active=True)
            if not teacher_profile.exists():
                messages.warning(request, "You're not allowed! Your ID has been deactivated. Please contact the administrator.")
                return render(request, 'base/not_to_access.html', {'page': "Not allowed!"})

        # Authenticate the user
        user_auth = authenticate(username=email, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect(reverse('attendence'))
        else:
            messages.warning(request, 'Invalid Password')
            return HttpResponseRedirect(request.path_info)

    context = {'page': 'User Login'}
    return render(request, 'teachers/login.html', context)



def logout_user(request):
    logout(request)
    return redirect('home')


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#     return redirect('login')