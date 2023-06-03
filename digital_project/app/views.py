from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Teacher, Student
from .forms import TeacherForm, StudentForm


def home(request):
    return render(request, 'home.html')


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def student_list(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        students = Student.objects.filter(teacher_id=teacher_id)
    else:
        students = []
    teachers = Teacher.objects.all()
    return render(request, 'student_list.html', {'students': students, 'teachers': teachers})
