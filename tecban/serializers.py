from rest_framework import serializers
from tecban.models import Terminal


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = [
            'id',
            'id_atm',
            'cd_atm',
            'ds_atm',
            'ds_logradouro',
            'nr_logradouro',
            'ds_bairro',
            'ds_cidade',
            'ds_uf',
            'ds_cep',
            'nr_long',
            'nr_lat',
            'id_status',
            'ds_horario_func',
            'fg_acessivel',
            'ds_segmento',
            'nr_segmento',
            'vl_cedula1',
            'vl_cedula2',
            'id_moedaestrang',
            'id_saquecom',
            'id_recicladora',
            'id_pgtocontas',
            'horario_inicial',
            'horario_final'
        ]
