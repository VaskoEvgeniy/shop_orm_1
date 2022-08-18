from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def product_view(request: HttpRequest,product_name : str)-> HttpResponse:
    product = {
        'name_shop': product_name

    }
    return render(request, "Product_page.html", product)