from django.shortcuts import render
from django.views.generic import TemplateView

stuff = ['Ветер', 'Лучик', 'Красный цвет']
text_title = 'Главная страница'
text_apologies = 'Простите, мы не умеем продавать'
text_button_buy = 'Купить'
text_button_back = 'На главную'

context = {
    'text_title': text_title,
    'stuff': stuff,
    'text_apologies': text_apologies,
    'text_button_buy': text_button_buy,
    'text_button_back': text_button_back
}


def main_market(request):
    template_name = 'task4_main.html'
    local_context = context
    return render(request, template_name, local_context)


def market(request):
    template_name = 'task4_market.html'
    local_context = context
    local_context['title'] = 'Магазин'
    return render(request, template_name, local_context)


def cart(request):
    template_name = 'task4_cart.html'
    local_context = context
    local_context['title'] = 'Корзина'
    return render(request, template_name, local_context)


def base(request):
    return render(request, 'menu.html', context)
