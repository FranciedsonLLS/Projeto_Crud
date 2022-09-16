from django.shortcuts import render, redirect
from django.http import HttpResponse 
import datetime
#importando cliente
from app.models import Cliente
from app.form import ClienteForm
#importando filme
from app.models import Filme
from app.form import FilmeForm
#importando reserva
from app.models import Reserva
from app.form import ReservaForm


# Create your views here.

def home(request):
    return render(request, "index.html")


# VIEWS DE CLIENTE (READ, CREATE, UPDATE, DELETE)#

def Lista_Clientes(request):    

    parametros = {"Clientes": Cliente.objects.all()}

    return render(request, "TelaClientes.html", parametros)

def Create_Clientes(request):   
    formCliente = ClienteForm(request.POST or None)
    form = {"FormCliente": formCliente}

    if formCliente.is_valid():
        formCliente.save()
        return redirect("/Clientes")
    
    return render(request, "FormClientes.html", form)

def Update_Clientes(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    formCliente = ClienteForm(request.POST or None, instance=cliente)

    if formCliente.is_valid():
        formCliente.save()
        return redirect('url_clientes')
        
    form = {"FormCliente": formCliente, "cliente": cliente}

    return render(request, 'FormClientes.html', form)

def Delete_Clientes(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_clientes')


# VIEWS DE FILMES (READ, CREATE, UPDATE, DELETE)#

def Lista_Filmes(request):    

    parametros = {"Filmes": Filme.objects.all()}

    return render(request, "TelaFilmes.html", parametros)

def Create_Filmes(request):   
    formFilme = FilmeForm(request.POST or None)
    form = {"FormFilme": formFilme}

    if formFilme.is_valid():
        formFilme.save()
        return redirect("/Filmes")
    
    return render(request, "FormFilmes.html", form)

def Update_Filmes(request, pk):
    filme = Filme.objects.get(pk=pk)
    formFilme = FilmeForm(request.POST or None, instance=filme)

    if formFilme.is_valid():
        formFilme.save()
        return redirect('url_filmes')
        
    form = {"FormFilme": formFilme, "filme": filme}

    return render(request, 'FormFilmes.html', form)

def Delete_Filmes(request, pk):
    filme = Filme.objects.get(pk=pk)
    filme.delete()
    return redirect('url_filmes')

# VIEWS DE RESERVAS (READ, CREATE, UPDATE, DELETE)#

def Lista_Reservas(request):    

    parametros = {"Reservas": Reserva.objects.all()}

    return render(request, "TelaReservas.html", parametros)

def Create_Reservas(request):   
    formReserva = ReservaForm(request.POST or None)
    form = {"FormReserva": formReserva}

    if formReserva.is_valid():
        formReserva.save()
        return redirect("/Reservas")
    
    return render(request, "FormReservas.html", form)

def Update_Reservas(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    formReserva = ReservaForm(request.POST or None, instance=reserva)

    if formReserva.is_valid():
        formReserva.save()
        return redirect('url_reservas')
        
    form = {"FormReserva": formReserva, "reserva": reserva}

    return render(request, 'FormReservas.html', form)

def Delete_Reservas(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    reserva.delete()
    return redirect('url_reservas')