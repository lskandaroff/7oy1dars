from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import *

# class CourseForm(forms.Form):
#     title = forms.CharField(max_length=100, widget=forms.TextInput())
#     description = forms.CharField(widget=forms.Textarea())


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput())
#     email = forms.EmailField(widget=forms.EmailInput())
#     course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select())

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email']

# def username_validator(value):
#     if ' ' in value:
#         raise ValidationError('usernameda bosh joy bolishi mumkun emas')
#
# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(), validators=[username_validator])
#     email = forms.EmailField(widget=forms.EmailInput())
#     password = forms.CharField(min_length=8, widget=forms.PasswordInput())
#     password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = self.cleaned_data.get('password')
#         password_repeat = self.cleaned_data.get('password_repeat')
#         if password_repeat != password:
#             raise ValidationError('parollar bir xil  bolishi kerak')
#
#         return cleaned_data

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput())
#     password = forms.CharField(min_length=8, widget=forms.PasswordInput())