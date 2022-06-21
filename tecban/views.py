import requests
from rest_framework.response import Response

from rest_framework.decorators import action, api_view


@api_view()
def find_terminal(request, *args, **kwargs):
    print(kwargs['id'])
    url = "https://api.homol.buscaatm.24horasdigital.com.br/v3/localizacaopc?pc=" + str(kwargs['id'])
    headers = {"Content-Type": "application/json", "x-api-key": "XaVmpwFgQU7sG9KZFbm50agQzgI5zw4satFE1FVJ"}
    response = requests.get(url, headers=headers).json()
    return Response(response)


@api_view()
def get_all_terminal(request, *args, **kwargs):
    latitude = str(request.GET.get('latitude', ''))
    longitude = str(request.GET.get('longitude', ''))
    url = "https://api.homol.buscaatm.24horasdigital.com.br/v3/localizacao?latitude=" + latitude + "&longitude=" + longitude + "&acessivel=0&lista=1&limite=10"
    headers = {"Content-Type": "application/json", "x-api-key": "XaVmpwFgQU7sG9KZFbm50agQzgI5zw4satFE1FVJ"}
    response = requests.get(url, headers=headers).json()
    return Response(response)
