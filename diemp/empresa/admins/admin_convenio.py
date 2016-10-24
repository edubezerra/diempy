from django.contrib import admin

class ConveniosModelAdmin(admin.ModelAdmin):
    list_display = ('id_empresa', 'numero')
    search_fields = ('id_empresa__nome', 'numero')

    def related_empresa(self, obj):
        return obj.id_empresa.nome
        related_empresa.short_description = 'Empresa'