from django.urls import path
from tecban.views import find_terminal, get_all_terminal

app_name = 'tecban'

urlpatterns = [
    path('tecban/find/<int:id>/', find_terminal, name='Find Terminal'),
    path('tecban/all', get_all_terminal, name='Get All Terminal'),
]
