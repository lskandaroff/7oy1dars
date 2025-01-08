from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('students/by/<int:course_id>/course/', students_by_course, name='students_by_course'),
    path('add/course/', add_course, name='add_course'),
    path('update/course/<int:course_id>/', course_update, name='course_update'),
    path('delete/course/<int:course_id>/', course_delete, name='course_delete'),
    path('delete/student/<int:student_id>/', student_delete, name='student_delete'),
    path('auth/register/', register, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('add/student/', add_student, name='add_student'),
    ]