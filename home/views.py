from django.shortcuts import render, redirect
from django.contrib.auth import logout

#Home page estática
def home(request):
    return render(request, 'home.html')

#Função para logout
def my_logout(request):
    logout(request)
    return redirect('home')