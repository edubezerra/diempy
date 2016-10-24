from django.contrib import admin

class PessoaCursoModelAdmin(admin.ModelAdmin):
    list_display = ('id_pessoa', 'matricula', 'id_curso')
    search_fields = ('id_pessoa__nome', 'matricula', 'id_curso__nome')