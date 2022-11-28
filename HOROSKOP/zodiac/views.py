from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Blok 1

def home(request):
    return HttpResponse('<h1>Main Page Horoscop</h1>')

def about(request):
    return HttpResponse('<h1>Page About</h1>')


zodiac_dict = {
    'Aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'Taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'Gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'Cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'Leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'Virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'Libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'Scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'Sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'Capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'Aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'Pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)'


}

sign_zodiak_dict =zodiac_dict.keys()

def get_sign(request, sign_name):
    description = zodiac_dict.get(sign_name, None)
    if description:
        return HttpResponse(f'<h1>{description}</h1>')
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака- {sign_name}")

def home_page(request):
    data={'header':list(zodiac_dict.keys()),
          'message':'это гороскоп'
          }

    return render(request, "home_page.html", context=data)

def zod(request):
    return render(request, "zod.html")



