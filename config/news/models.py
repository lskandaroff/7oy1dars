from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='users/photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    level = models.CharField(max_length=150, null=True, blank=True)
    web_site = models.CharField(max_length=150, null=True, blank=True)
    github = models.CharField(max_length=150, null=True, blank=True)
    telegram = models.CharField(max_length=150, null=True, blank=True)
    instagram = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('students_by_course', kwargs={'course_id': self.course.id})
