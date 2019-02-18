from django.shortcuts import render
from .models import Filmes
from .forms import FilmesForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#Cadastra os elementos da classe Filmes com cbv
class Filmes_Create(LoginRequiredMixin,CreateView): 
    model=Filmes
    fields = ['nome','descricao','url']
    success_url = '/filmes/list'

#Lista os filmes cadastrados
class Filmes_List(ListView):
    model= Filmes

#Exibi detalhes de filmes com detailview
class Filmes_Detail(DetailView):
    model=Filmes

#Altera a descrição do filme
class Filmes_Update(LoginRequiredMixin,UpdateView):
    model= Filmes
    fields = ['descricao']
    success_url = '/filmes/list'

#Deletar Filme
class Filmes_Delete(LoginRequiredMixin,DeleteView):
    model=Filmes
    success_url = '/filmes/list'

#cadastrar usuário
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})