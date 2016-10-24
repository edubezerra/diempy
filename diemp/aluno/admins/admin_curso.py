from django.contrib import admin


class CursosModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade')
    search_fields = ('nome', 'unidade')

    readonly_fields = ('nome', 'unidade', 'cod_curso')