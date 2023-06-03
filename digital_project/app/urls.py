from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
]
