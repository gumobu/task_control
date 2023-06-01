from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def issues_list(request):
    return render(request, 'issue/issues_list.html', locals())


def issue_detail(request, issue_id):
    """Отображение подробной информации о задаче"""
    return render(request, 'issue/issue_detail.html', locals())
