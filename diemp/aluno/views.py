from io import TextIOWrapper
import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from diemp.aluno.forms import ImportForm
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso
from diemp.aluno.models.model_pessoacurso import PessoaCurso


def new(request):
    if not request.user.is_authenticated():
        return call_login(request)
    else:
        return create(request)


def call_login(request):
    return HttpResponseRedirect(r('login:login'))


def create(request):
    if request.method == "POST":
        form = ImportForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'aluno/import_csv.html', {'form': form})
        try:
            handle_files(request)
        except:
            return render(request, 'aluno/import_csv.html', {'form': form, 'error': True})
        return render(request, 'aluno/import_csv.html', {'form': form, 'success': True})
    return render(request, 'aluno/import_csv.html', {'form': ImportForm()})


def handle_files(request):
    f = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
    reader = csv.reader(f)
    cont = 0
    for row in reader:
        if cont != 0 :
            NOME = row[0]
            MATRICULA = row[1]
            COD_CURSO = row[2]
            CPF = row[4]
            SITUACAO = row[6]
            DDI_RESIDENCIAL = row[7]
            DDD_RESIDENCIAL = row[8]
            FONE_RESIDENCIAL = row[9]
            DDI_COMERCIAL = row[10]
            DDD_COMERCIAL = row[11]
            FONE_COMERCIAL = row[12]
            DDI_CELULAR = row[13]
            DDD_CELULAR = row[14]
            FONE_CELULAR = row[15]
            TIPO_LOGRADOURO = row[16]
            LOGRADOURO = row[17]
            NUMERO = row[18]
            COMPLEMENTO = row[19]
            BAIRRO = row[20]
            CEP = row[21]
            DISTRITO = row[22]
            MUNICIPIO = row[23]
            UF = row[24]
            PAIS = row[25]
            EMAIL = row[26]
            DT_NASC = row[27].split('/')
            DT_NASC = (DT_NASC[2] + '-' + DT_NASC[1] + '-' + DT_NASC[0])

            obj = Inscricao(nome=NOME, email=EMAIL, cpf=CPF, dt_nasc=DT_NASC, situacao=SITUACAO,
                            ddi_residencial=DDI_RESIDENCIAL, ddd_residencial=DDD_RESIDENCIAL,
                            fone_residencial=FONE_RESIDENCIAL,
                            ddi_comercial=DDI_COMERCIAL, ddd_comercial=DDD_COMERCIAL, fone_comercial=FONE_COMERCIAL,
                            ddi_celular=DDI_CELULAR, ddd_celular=DDD_CELULAR, fone_celular=FONE_CELULAR,
                            tipo_logradouro=TIPO_LOGRADOURO,
                            logradouro=LOGRADOURO, numero=NUMERO, complemento=COMPLEMENTO, bairro=BAIRRO, cep=CEP,
                            distrito=DISTRITO,
                            municipio=MUNICIPIO, uf=UF, pais=PAIS)

            try:
                objAluno = Inscricao.objects.get(cpf=CPF)
                id = objAluno.pk
            except:
                id = None

            if id:
                obj.id = id
            obj.save()

            obj_curso = Curso.objects.get(cod_curso=COD_CURSO)
            try:
                objpessoacurso = PessoaCurso.objects.get(id_pessoa=obj.pk)
            except:
                objpessoacurso = None
            if objpessoacurso:
                if (objpessoacurso.id_curso == obj_curso.pk):
                    continue

            obj_ps = PessoaCurso(Curso=obj_curso, Aluno=obj, Matrícula=MATRICULA)
            obj_ps.save()
        else:
            cont += 1
    return True