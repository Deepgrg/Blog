from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User

# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required

from .forms import UserRegisterForm


def registerPage(request):
    form = UserRegisterForm()
    if request.method =="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('user_page')
    context={
        'form' : form,
        'title' : 'Register',
    }
    return render(request , 'account/registerPage.html' , context)


def loginPage(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('user_page' , user.pk )
        else:
            messages.warning(request, 'Username or Password is incorrect')
    context={

    }
    return render(request , 'account/loginPage.html' , context)


@login_required
def logoutPage(request):
    logout(request)
    return redirect('index_page')


# @login_required(login_url='login_page')
def userPage(request, pk):
    user = User.objects.get(id = pk)
    context={
        'user' : user,
    }
    return render(request, 'account/userPage.html', context)