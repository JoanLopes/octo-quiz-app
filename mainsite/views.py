from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.models import User
from .forms import RegisterForm

import logging

logger = logging.getLogger('mainsite')

class Login(View):
    def get(self, request):
        contexto = {'mensagem': ""}

        if not request.user.is_authenticated:
            return render(request, "autenticacao.html", contexto)
        else:
            return render(request, 'home.html', {'usuario': request.user.username})


    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        logger.info(f'Usuário: {usuario}')
        logger.info(f'Senha: {senha}')
        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {'usuario': user.username})
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo.'})
        
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválida.'})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'autenticacao.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Loga o usuário automaticamente
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, 'Registration successful. Welcome!')
                return redirect('/veiculo')
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, 'autenticacao.html', {'form': form})
