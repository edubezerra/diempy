from django.conf.urls import url, include

from django.contrib import admin
from diemp.core.views import home

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^aluno/', include('diemp.aluno.urls', namespace='aluno')),
    url(r'^login/', include('diemp.login.urls', namespace='login')),
]