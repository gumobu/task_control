from django.shortcuts import render


def main(request):
    title = 'Главная страница системы контроля и управления задачами'
    return render(request, 'mainpage/main_page.html', locals())
