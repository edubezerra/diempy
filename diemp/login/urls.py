from django.conf.urls import url

from diemp.login.views import new, call_logout

urlpatterns = [
    url(r'^$', new, name='login'),
    url(r'^logout/$', call_logout, name='logout'),
]