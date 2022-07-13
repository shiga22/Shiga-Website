from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from accounts.forms import UserForm ,UserProfileInfoForm ,CourseProfileInfoform ,TaskInfoform
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import  CourseProfileInfo,TaskInfo


# Create your views here.
def Index(request):
    return render(request,'home.html')

def register(request):
    
    registered= False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
     
            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors , profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/registration.html',
                           { 'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
    else:
        return render(request,'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def Course(request):
    registered =False
    if request.method =="POST":
        course_form =CourseProfileInfoform(data=request.POST)

        if course_form.is_valid():
            program =course_form.save(commit=False)
            program.save()
            registered=True
        else:
             print(course_form.errors)
    else:
        course_form =CourseProfileInfoform()
    return render(request, 'accounts/Course.html',
                            {'registered':registered,
                             'course_form':course_form})


def display(request):
    picture = CourseProfileInfo.objects.all
    context={'picture':picture}
    return render(request,'accounts/course_display.html',context)


def Task(request):
    registered =False
    if request.method =="POST":
        task_form =TaskInfoform(data=request.POST)

        if task_form.is_valid():
            program =task_form.save(commit=False)
            program.save()
            registered=True
        else:
             print(task_form.errors)
    else:
        task_form =TaskInfoform()
    return render(request, 'accounts/Task.html',
                            {'registered':registered,
                             'task_form':task_form})


def displayTask(request):
    picture = TaskInfo.objects.all
    context={'picture':picture}
    return render(request,'accounts/task_display.html',context)

