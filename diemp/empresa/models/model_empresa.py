from django.db import models
from diemp.empresa.validators import validate_cnpj


class Empresa(models.Model):
    numero = models.IntegerField(db_column='Numero', unique=True, blank=True, null=True)
    nome = models.CharField(db_column='Nome', max_length=100)
    cnpj = models.CharField(db_column='Cnpj', max_length=100,  validators=[validate_cnpj])


    class Meta:
        managed = False
        db_table = 'empresa'
        verbose_name_plural = 'empresas'
        verbose_name = 'empresa'
        ordering = ('nome',)

    def __str__(self):
        return self.nome