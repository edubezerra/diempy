from django.db import models
from diemp.aluno.models.model_aluno import Inscricao
from diemp.empresa.models.model_convenio import Convenio

class Estagio(models.Model):
    data_inicio_vigencia = models.DateField(db_column='Data_Inicio_Vigencia')
    data_fim_vigencia = models.DateField(db_column='Data_Fim_Vigencia')
    data_rescisao = models.DateField(db_column='Data_Rescisao', blank=True, null=True)
    #data_aditivo = models.DateField(db_column='Data_Aditivo', blank=True, null=True)
    id_aluno = models.ForeignKey(Inscricao, db_column='id_aluno', verbose_name='Aluno')
    id_convenio = models.ForeignKey(Convenio, db_column='id_convenio', verbose_name='Convenio')
    estado = models.CharField(db_column='Estado', max_length=10, choices = [('Em Andamento', 'Em Andamento'), ('Terminado', 'Terminado'), ('Aguardando Documentos', 'Aguardando Documentos'), ('Termo Aditivo', 'Termo Aditivo'), ('Cancelado', 'Cancelado')])

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.data_inicio_vigencia > self.data_fim_vigencia:
            raise ValidationError('A data de início deve ser menor que a de fim')

    class Meta:
        managed = False
        db_table = 'estagio'
        verbose_name_plural = 'estagios'
        verbose_name = 'estagio'
        ordering = ('-data_inicio_vigencia',)