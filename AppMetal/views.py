from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppMetal.forms import *

def inicio(request):
    return render(request, "AppMetal/inicio.html", {'isMain': 1})

def ingresantes(request):
    return render(request, "AppMetal/ingresantes.html")

def graduados(request):
    return render(request, "AppMetal/graduados.html")

def banda(request):
    return render(request, "AppMetal/banda.html")

def ingreFormulario(request):
    if request.method=="POST":
        form=IngresantesForm(request.POST)
        print("-----------------")
        print(form)
        print("-----------------")
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            instrumento=informacion["instrumento"]
            ingre=Ingresantes(nombre=nombre, apellido=apellido, instrumento=instrumento)
            ingre.save()
            return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    else:
        form=IngresantesForm
        return render (request, "AppMetal/ingreFormulario.html", {"formulario":form})


def graduadosFormulario(request):
    if request.method=="POST":
        form= GraduadosForm(request.POST)
        print("-----------------")
        print(form)
        print("-----------------")
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            instrumento=info["instrumento"]
            graduado=Graduados(nombre=nombre, apellido=apellido, instrumento=instrumento)
            graduado.save()
            return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    else:
        form=GraduadosForm
        return render (request, "AppMetal/graduadosformulario.html", {"formulario":form})


def bandasFormulario(request):
    if request.method=="POST":
        nombre=request.POST["Nombre"]
        comision=request.POST["Comision"]
        banda=Bandas(nombre=nombre, comision=comision)
        banda.save()
        return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    
    return render (request, "AppMetal/bandasFormulario.html")



def busquedaIngresante(request):
    return render(request, "Appmetal/busquedaIngresante.html")

def busquedaIngre(request):
    if request.GET["nombre"]:
        if request.GET["nombre"] == "all":
            ingresante = Ingresantes.objects.all()
        else:
            nombre=request.GET["nombre"]
            ingresante=Ingresantes.objects.filter(nombre=nombre)
        return render (request, "AppMetal/resultadoIngresante.html", {"ingresante":ingresante})
    else:
        return render(request, "AppMetal/ingresantes.html", {"mensaje":"invalid"})
    


def busquedaGraduado(request):
    return render(request, "Appmetal/busquedaGraduados.html")

def busquedaGra(request):
    if request.GET["nombre"]:
       if request.GET["nombre"] == "all":
          graduado=Graduados.objects.all()
       else:
          nombre=request.GET["nombre"]
          graduado=Graduados.objects.filter(nombre=nombre)
       return render (request, "AppMetal/resultadoGraduados.html", {"graduado":graduado})
    else:
       return render(request, "AppMetal/graduados.html", {"mensaje":"invalid"})
    


def busquedaBanda(request):
    return render(request, "Appmetal/busquedaBanda.html")

def busquedaBan(request):
    if request.GET["nombre"]:
        if request.GET["nombre"] == "all":
            banda = Bandas.objects.all()
        else:
            nombre=request.GET["nombre"]
            banda=Bandas.objects.filter(nombre=nombre)
        return render (request, "AppMetal/resultadoBanda.html", {"banda":banda})
    else:
        return render(request, "AppMetal/banda.html", {"mensaje":"invalid"})
    
    