from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'home.html', context)

def students_by_course(request, course_id):
    students = get_list_or_404(Student, course_id=course_id)

    context = {
        'students': students
    }

    return render(request, 'students_by_course.html', context)

@permission_required('news.add_course', raise_exception=True)
def add_course(request: WSGIRequest):

 if request.method == 'POST':
     form = CourseForm(data=request.POST, files=request.FILES)
     if form.is_valid():
         course = Course.objects.create(**form.cleaned_data)
         print(course, 'qoshildi!')


 forms = CourseForm()
 context = {
  'forms': forms
 }
 return render(request, 'course_add.html', context)

@permission_required('news.update_course', raise_exception=True)
def course_update(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course.title = form.cleaned_data.get('title')
            course.description = form.cleaned_data.get('description')
            course.save()
            messages.success(request, 'Course ozgartirildi')
            return redirect('home')

    forms = CourseForm(initial={
        'title': course.title,
        'description': course.description
    })

    context = {
        'forms': forms
    }

    return render(request, 'course_add.html', context)

@permission_required('news.delete_course', raise_exception=True)
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course ochirildi')
        return redirect('home')

    context = {
        'course': course
    }

    return render(request, 'confirm_delete.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, 'Xush kelibsiz')
            login(request, user)
            return redirect('home')
    context = {
        'form': LoginForm()
    }

    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                user = MyUser.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Royxatdan otildi')
                return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'auth/register.html', context)
