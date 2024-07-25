from django import forms
from .models import Classroom,Tutorial, Discussion

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'description', 'code']


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'pdf']

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['content']