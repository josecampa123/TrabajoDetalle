from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entre

# Create your views here.

class DetaListView(ListView):
    model = Entre
    template_name = 'home.html'
    context_object_name = 'carpeta'


class DetaDetailView(DetailView):
    model = Entre
    template_name = 'archivo.html'
    context_object_name = 'carpeta'

class notaCreateView(CreateView):
    model = Entre
    template_name = "notaNueva.html"
    fields = '__all__'



class notaEditar(UpdateView):
    model = Entre
    template_name = 'editarJuego.html'
    fields = ['juego','Descripcion']


class notaDeleteView(DeleteView):
    model = Entre
    template_name = 'eliminarJuego.html' 
    context_object_name = 'carpeta'
    success_url = reverse_lazy('home')
