from django.urls import path
from AppMetal.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("ingresante/", ingresantes, name= "ingresante"),
    path("graduado/", graduados, name= "graduado"),
    path("banda/", banda, name= "banda"),
    path("resultadobanda/", busquedaBan, name="busquedaBan"),
    path("resultadoIngresante/", busquedaIngre, name="busquedaIngre"),
    path("resultadogradudado/", busquedaGra, name="busquedaGra"),
    path("addIngresante/", ingreFormulario, name="ingreFormulario"),
    path("addBanda/", bandasFormulario, name="bandasFormulario"),
    path("addGraduado/", graduadosFormulario, name="graduadosFormulario"),

    #path("ingresantes/", ingreFormulario, name="ingreFormulario"),
    #path("graduados/", graduadosFormulario, name="graduadosFormulario"),
    #path("bandas/", bandasFormulario, name="bandasFormulario"),
    #path("busquedaingresante/", busquedaIngresante, name="busquedaIngresante"),
    #path("busquedagraduado/", busquedaGraduado, name="busquedaGraduados"),
    #path("busquedabanda/", busquedaBanda, name="busquedaBandas"),
]
