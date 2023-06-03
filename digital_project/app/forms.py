from django import forms
from .models import Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'email')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'teacher')

    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
