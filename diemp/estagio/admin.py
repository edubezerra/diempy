from django.contrib import admin
from diemp.estagio.models import Estagio


class EstagiosModelAdmin(admin.ModelAdmin):
    list_display = ('id_aluno', 'id_convenio')
    search_fields = ('id_aluno__nome', 'id_convenio__id_empresa__nome')

    def related_estagio(self, obj):
        return obj.id_aluno.nome
        related_estagio.short_description = 'Estagio'

    def related_convenio(self, obj):
        return obj.id_convenio.numero
        related_convenio.short_description = 'Convenio'

admin.site.register(Estagio, EstagiosModelAdmin)

