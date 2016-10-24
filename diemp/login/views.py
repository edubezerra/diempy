from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from diemp.login.forms import LoginForm


def new(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            return create(request)
        return empty_form(request)
    else:
        return call_import(request)


def create(request):
    form = LoginForm(request.POST)

    if not form.is_valid():
        return render(request, 'login/login.html', {'form': form})

    user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

    if user is not None:
        login(request, user)
        return call_import(request)
    else:
        return render(request, 'login/login.html', {'form': form})


def empty_form(request):
    return render(request, 'login/login.html', {'form': LoginForm()})


def call_import(request):
    return HttpResponseRedirect(r('aluno:aluno'))


def call_logout(request):
    logout(request)
    return HttpResponseRedirect(r('login:login'))