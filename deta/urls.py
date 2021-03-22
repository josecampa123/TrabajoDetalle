from django.urls import path
from.views import (
    DetaListView, 
    DetaDetailView,
    notaCreateView,
    notaEditar,
    notaDeleteView
    

) 

urlpatterns = [
    path('nota/<int:pk>/eliminar',  notaDeleteView.as_view(), name="eliminarJuego"),
    path('nota/<int:pk>/editar', notaEditar.as_view(), name="editarJuego"),
    path('nota/Nueva', notaCreateView.as_view(), name="notaNueva"),
    path('nota/<int:pk>/', DetaDetailView.as_view(), name='archivo'),
    path('', DetaListView.as_view(), name='home')
]