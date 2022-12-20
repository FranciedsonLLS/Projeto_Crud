from tkinter import CASCADE
from django.db import models


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=124, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.TextField(max_length=9, null=True, blank=True)
    bairro = models.CharField(max_length=124, null=True, blank=True)
    rua = models.CharField(max_length=124, null=True, blank=True)
    num_casa = models.TextField(max_length=4, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=124)
    autor = models.CharField(max_length=124)
    duracao = models.DurationField()
    GENERO_CHOICES = (
        ("Terror","Terror"),
        ("Comédia","Comédia"),
        ("Ação","Ação"),
        ("Romance","Romance"),
        ("Aventura","Aventura"),
        ("Suspense","Suspense"),
        ("Ficção Científica","Ficção Científica"),
        ("Drama","Drama"),
        ("Documentário","Documentário"),
        ("LGBTQ","LGBTQ"),
    )
    genero = models.CharField(max_length=20,choices=GENERO_CHOICES, blank=False, null=False)
    data_criacao = models.DateField()
    
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete= models.CASCADE) 
    STATUS_CHOICES = (
        ("PENDENTE","PENDENTE"),
        ("ENTREGUE","ENTREGUE"),
        ("DEVOLVIDO","DEVOLVIDO"),
    )   
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, blank=False, null=False)
    class Meta:
        verbose_name_plural = "Reservas"
    





