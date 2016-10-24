from django.contrib import admin


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')

    readonly_fields = ('nome', 'email', 'cpf', 'dt_nasc', 'situacao',
                       'ddi_residencial', 'ddd_residencial', 'fone_residencial', 'ddi_comercial',
                       'ddd_comercial', 'fone_comercial', 'ddi_celular', 'ddd_celular', 'fone_celular',
                       'tipo_logradouro', 'logradouro', 'numero', 'complemento', 'bairro', 'cep',
                       'bairro', 'cep', 'distrito', 'municipio', 'uf', 'pais')