from django.shortcuts import render, HttpResponseRedirect
from .forms import CoursForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = CoursForm(request)
        return render(request,"SAE_GA/Cours/ajout.html",{"form" : form, "id": None})
    else :
        form = CoursForm()
        return render(request,"SAE_GA/Cours/ajout.html",{"form" : form})

def traitement(request):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        cours = lform.save()
        return HttpResponseRedirect("/SAE_GA/Cours/accueil")
    else :
        return render(request, "SAE_GA/Cours/ajout.html", {"form" : lform})

def accueil(request):
    liste = list(models.Cours.objects.all())
    return render(request,"SAE_GA/Cours/accueil.html",{'liste' : liste})

def affiche(request, id):
    cours = models.Cours.objects.get(pk=id)
    return render(request, "SAE_GA/Cours/affiche.html",{"cours" : cours})

def update(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(cours.__dict__)
    return render(request,"SAE_GA/Cours/ajout.html",{"form" : form, "id" : id})

def updatetraitement(request, id):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        cours = lform.save(commit=False)
        cours.id = id
        cours.save()
        return HttpResponseRedirect("/SAE_GA/Cours/accueil")
    else :
        return render(request, "SAE_GA/Cours/ajout.html", {"form" : lform, "id": id})

def delete(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/SAE_GA/Cours/accueil")