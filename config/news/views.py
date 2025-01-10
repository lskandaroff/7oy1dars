from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    courses = Course.objects.all()

    paginator = Paginator(courses, 2)

    page = request.GET.get('page', 1)


    context = {
        'page_objects': paginator.page(page),
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
         messages.success(request, 'kurs qoshildi')
         return redirect('home')


 forms = CourseForm()
 context = {
  'forms': forms
 }
 return render(request, 'course_add.html', context)

@permission_required('news.add_students', raise_exception=True)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # student = Student.objects.create(**form.cleaned_data)
            form.save()
            messages.success(request, 'Talaba qoshildi')
            return redirect('home')

    forms = StudentForm()
    context = {
        'forms': forms
    }
    return render(request, 'add_student.html', context)

def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Talaba ochirildi')
        return redirect('home')
    context = {
        'student': student
    }

    return render(request, 'confirm_delete.html', context)


@permission_required('news.update_course', raise_exception=True)
def course_update(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES, instance=course)
        if form.is_valid():
            # course.title = form.cleaned_data.get('title')
            # course.description = form.cleaned_data.get('description')
            course.save()
            messages.success(request, 'Course ozgartirildi')
            return redirect('home')

    forms = CourseForm(instance=course)

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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Xush kelibsiz')
            login(request, user)
            return redirect('home')
    context = {
        'form': AuthenticationForm()
    }

    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Royxatdan otildi')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'auth/register.html', context)


def send_message_to_email(request):
    if request.method == 'POST':
        form = EmailForm(data=request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            users = MyUser.objects.all()
            for user in users:
                send_mail(subject,
                          message,
                          'dostoniskandarov0204@gmail.com',
                          [user.email],
                          fail_silently=False)
                messages.success(request, 'email jonatildi')
                return redirect('home')
    else:
        form = EmailForm()
    context = {
            'form': form
            }
    return render(request, 'send_email.html', context)
