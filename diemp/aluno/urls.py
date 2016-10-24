from django.conf.urls import url

from diemp.aluno.views import new

urlpatterns = [
    url(r'^$', new, name='aluno'),
]