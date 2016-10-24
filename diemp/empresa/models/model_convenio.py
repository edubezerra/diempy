from django.db import models
from diemp.empresa.models.model_empresa import Empresa

class Convenio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    numero = models.CharField(db_column='Numero', unique=True, max_length=10)
    id_empresa = models.ForeignKey(Empresa, db_column='id_empresa', verbose_name="empresa")
    data_inicio = models.DateField(max_length=11)
    data_fim = models.DateField(max_length=11)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.data_inicio > self.data_fim:
            raise ValidationError('A data de início deve ser menor que a de fim')


    class Meta:
        managed = False
        db_table = 'convenio'
        verbose_name_plural = 'convenios'
        verbose_name = 'convenio'
        ordering = ('id_empresa__nome',)

    def __str__(self):
        return self.id_empresa.nome