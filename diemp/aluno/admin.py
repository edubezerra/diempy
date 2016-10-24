from django.contrib import admin
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso
from diemp.aluno.models.model_pessoacurso import PessoaCurso
from diemp.aluno.admins.admin_aluno import InscricaoModelAdmin
from diemp.aluno.admins.admin_curso import CursosModelAdmin
from diemp.aluno.admins.admin_pessoacurso import PessoaCursoModelAdmin

admin.site.register(Inscricao, InscricaoModelAdmin)
admin.site.register(Curso, CursosModelAdmin)
admin.site.register(PessoaCurso, PessoaCursoModelAdmin)