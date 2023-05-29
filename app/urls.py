from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.Inicio, name="Indice"),
    path('entradas/', views.Entradas, name="Entradas"),
    # nos indica el camino '' esto significa que es la pagina principal, despues de la coma nos dice que funcion va a devolver
    path('salidas/', views.Salidas, name="Salidas"),
    path('registroentradas/', views.RegistroEntradas, name="RegistroEntradas"),
    path('registrosalidas/', views.RegistroSalidas, name="RegistroSalidas"),
    path('eliminarentrada/<int:id_entrada>', views.EliminarEntrada, name="EliminarEntrada"),
    path('editarentrada/<int:id_entrada>', views.EditarEntrada, name="EditarEntrada"),
    path('eliminarsalida/<int:id_salida>', views.EliminarSalida, name="EliminarSalida"),
    path('editarsalida/<int:id_salida>', views.EditarSalida, name="EditarSalida"),
    path('exportar-a-excel/', views.exportar_a_excel, name='exportar_a_excel'),
    path('', views.AbrirSesion, name='Login'),
    path('signup/', views.Signup, name='Signup'),
    path('cerrarsesion/', views.CerrarSesion, name='CerrarSesion'),
    path('nosotros/', views.Nosotros, name='Nosotros'),
    path('productos/', views.Productos, name='Productos'),
]
