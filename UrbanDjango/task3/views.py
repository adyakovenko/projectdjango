from django.shortcuts import render
from django.views.generic import TemplateView

def MainMarket(request):
    template_name = 'task3_main.html'
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, template_name, context)


def market(request):
    template_name = 'task3_market.html'
    context = {
        'buy': 'Купить',
        'wind': 'Ветер',
        'ray': 'Лучик',
        'red': 'Красный цвет'
    }
    return render(request, template_name, context)


def cart(request):
    template_name = 'task3_cart.html'
    apologies = 'Простите, мы пока не умеем покупать.'
    context = {'sorry': apologies}
    return render(request, template_name, context)