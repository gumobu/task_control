from django import forms
from .models import Issue


class AddIssue(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'project', 'description', 'plan_end_date', 'parent_issue', 'assignee', 'watcher',)


class UpdateIssue(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('description', 'assignee', 'watcher', 'status')