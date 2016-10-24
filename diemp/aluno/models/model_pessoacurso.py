from django.db import models
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso


class PessoaCurso(models.Model):
    matricula = models.CharField(db_column='Matricula', max_length=100, verbose_name='Matrícula')
    id_curso = models.ForeignKey(Curso, db_column='ID_CURSO', verbose_name='Curso')
    id_pessoa = models.ForeignKey(Inscricao, db_column='Id_Pessoa',  verbose_name='Aluno')

    class Meta:
        managed = False
        db_table = 'pessoa__curso'