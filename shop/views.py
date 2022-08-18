from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import random

def random_cost():
    cost = random.randint(10000, 20000)
    return cost

def homepage(request: HttpRequest)-> HttpResponse:
    home_page = {
        'username': 'anonim_user',
        'cost_item': random_cost,
        'item_name': ['Rozenta', 'Roznica', 'Comfy'],
    }
    return render(request,'Home_page.html', home_page)

def homepage_views(request: HttpRequest, username: str) -> HttpResponse:


    custom_ctx_obj = {
        'username': username,

        'cost_item': random_cost,
        'item_name': ['Rozenta', 'Roznica', 'Comfy'],

    }
    return render(request, 'Home_page.html', custom_ctx_obj)

