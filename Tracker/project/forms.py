from django import forms
from .models import Project


class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',)
