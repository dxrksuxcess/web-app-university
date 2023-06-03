from django.shortcuts import render, get_object_or_404

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
        students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'student_list.html', {'students': students, 'teachers': teachers})


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teacher_list')


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
