from django.contrib import admin
from diemp.empresa.models.model_convenio import Convenio
from diemp.empresa.models.model_empresa import Empresa
from diemp.empresa.admins.admin_empresa import EmpresaModelAdmin
from diemp.empresa.admins.admin_convenio import ConveniosModelAdmin


admin.site.register(Empresa, EmpresaModelAdmin)
admin.site.register(Convenio, ConveniosModelAdmin)