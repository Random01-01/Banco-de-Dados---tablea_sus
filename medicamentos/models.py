# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Doenca(models.Model):
    id_doenca = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'doenca'


class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'medicamento'


class Preco(models.Model):
    id_preco = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    valor_medio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preco'


class Tratamento(models.Model):
    id_tratamento = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    id_doenca = models.ForeignKey(Doenca, models.DO_NOTHING, db_column='id_doenca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamento'
