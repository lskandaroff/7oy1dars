from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='users/photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

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
