from django.forms import ModelForm
from .models import Filmes

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'descricao', 'url']

        def __str__(self):
            return self.nome