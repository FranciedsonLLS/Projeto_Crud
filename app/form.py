from django.forms import ModelForm
from .models import Cliente, Filme, Reserva

##Criando CLIENTE

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'telefone', 'bairro', 'rua', 'num_casa']

#Criando FILME
class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'autor', 'duracao', 'genero', 'data_criacao']

#Criando RESERVA

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'filme', 'status', ]

