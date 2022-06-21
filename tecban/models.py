from django.db import models
import uuid


class Terminal(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    id_atm = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    cd_atm = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_atm = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_logradouro = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    nr_logradouro = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_bairro = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_cidade = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_uf = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_cep = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    nr_long = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    nr_lat = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    id_status = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_horario_func = models.CharField(
        max_length=100,
        null=False,
        blank=True)

    fg_acessivel = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    ds_segmento = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    nr_segmento = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    vl_cedula1 = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    vl_cedula2 = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    id_moedaestrang = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    id_saquecom = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    id_recicladora = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    id_pgtocontas = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    horario_inicial = models.CharField(
        max_length=30,
        null=False,
        blank=True)

    horario_final = models.CharField(
        max_length=30,
        null=False,
        blank=True)
