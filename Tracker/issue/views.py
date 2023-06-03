from django.shortcuts import render, redirect
from .models import *
from .forms import *


def issues_list(request):
    title = 'Список задач системы'
    page_title = 'Список существующих задач'
    issues = Issue.objects.all().order_by('id')
    return render(request, 'issue/issues_list.html', locals())


def issue_detail(request, issue_id):
    """Отображение подробной информации о задаче"""
    issue = Issue.objects.get(id=issue_id)
    child_issues = issue.child.all()
    return render(request, 'issue/issue_detail.html', locals())


def create_issue(request):
    """Форма создания задачи"""
    if request.method == 'POST':
        form = AddIssue(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.updated_date = timezone.now()
            issue.status = 'CRT'
            issue = form.save()
            return redirect('issue', issue_id=issue.id)
    else:
        form = AddIssue()
    return render(request, 'issue/create_issue.html', locals())


def update_issue(request, issue_id):
    """Форма обновления задачи"""
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        form = UpdateIssue(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.updated_date = timezone.now()
            if issue.status in ('DCL', 'END'):
                issue.fact_end_date = timezone.now()
            issue = form.save()
        return redirect('issue', issue_id=issue.id)
    else:
        form = UpdateIssue(instance=issue)
    return render(request, 'issue/update_issue.html', locals())