from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request, 'userAccount/login.html')


# users
def users(request):
    return render(request, 'userAccount/users.html')
