from django.urls import path

from .views import *

urlpatterns = [
    # class
    path('send/email/', SendEmailView.as_view(), name='send_message_to_email'),
    path('', PostListView.as_view(), name="home"),
    path('students/by/<int:course_id>/course/', PostDetailView.as_view(), name='students_by_course'),
    path('add/student/', AddStudentView.as_view(), name='add_student'),
    path('update/student/<int:student_id>/', UpdateStudentsView.as_view(), name='update_student'),
    path('delete/student/<int:student_id>/', DeleteStudentsView.as_view(), name='student_delete'),
    path('auth/profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    # function
    # path('', home, name="home"),
    # path('students/by/<int:course_id>/course/', students_by_course, name='students_by_course'),
    path('add/course/', add_course, name='add_course'),
    path('update/course/<int:course_id>/', course_update, name='course_update'),
    path('delete/course/<int:course_id>/', course_delete, name='course_delete'),
    # path('delete/student/<int:student_id>/', student_delete, name='student_delete'),
    path('auth/register/', register, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    # path('add/student/', add_student, name='add_student'),
    # path('send/email/', send_message_to_email, name='send_message_to_email'),
    ]