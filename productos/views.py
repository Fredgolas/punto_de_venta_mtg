from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Card

# Create your views here.

class CardListInventory(ListView):
    model = Card


class CardCreateView(CreateView):
    model = Card
    #fields = ['name','price','quantity','types','set','collector_number','condition','finish']
    fields = '__all__'
    success_url = '/inventario/'

class CardUpdateView(UpdateView):
    model = Card
    fields = '__all__'
    #exclude = ['img']
    template_name_suffix = "_update_form"
    success_url = '/inventario/'

class CardDeleteView(DeleteView):
    model = Card
    success_url = '/inventario/'
