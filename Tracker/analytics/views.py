from django.shortcuts import render
from django.db.models import Count, Q, F
from project.models import Project
from issue.models import Issue
from account.models import Profile


def analytics_main(request):
    page_title = "Выберите способ вывода аналитических данных"
    title = "Аналитика"
    return render(request, 'analytics/analytics_main.html', locals())


def by_projects(request):
    page_title = 'Аналитика в разбивке по проектам'
    title = 'Аналитика в разбивке по проектам'
    projects = Project.objects.annotate(
        open=(Count('issues', filter=Q(issues__status__in=['ANA', 'WRK']))),
        close=(Count('issues', filter=Q(issues__status__in=['DCL', 'END']))),
        total=(Count('issues')),
        overdue=(Count('issues', filter=(Q(issues__fact_end_date__isnull=False) &
                                         Q(issues__fact_end_date__gt=F('issues__plan_end_date')))))
    )
    return render(request, 'analytics/by_projects.html', locals())


def by_users(request):

    pass
