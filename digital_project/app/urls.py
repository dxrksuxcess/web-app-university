from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('edit_teacher/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]
