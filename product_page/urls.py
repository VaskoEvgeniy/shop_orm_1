from django.urls import path
from product_page.views import product_view


urlpatterns = [
    path('<str:product_name>/', product_view, name='product')
]