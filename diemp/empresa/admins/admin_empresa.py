from django.contrib import admin
from django.forms import TextInput
from django.db import models


class EmpresaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})}
    }