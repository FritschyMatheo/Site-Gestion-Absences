from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = EnseignantForm(request)
        return render(request,"SAE_GA/Enseignant/ajout.html",{"form" : form})
    else :
        form = EnseignantForm()
        return render(request, "SAE_GA/Enseignant/ajout.html", {"form" : form})

def traitement(request):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        enseignant = lform.save()
        return HttpResponseRedirect("/SAE_GA/Enseignant/accueil")
    else :
        return render(request, "SAE_GA/Enseignant/ajout.html", {"form" : lform})


def accueil(request):
    liste = list(models.Enseignant.objects.all())
    return render(request,"SAE_GA/Enseignant/accueil.html",{'liste' : liste})


def affiche(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    return render(request, "SAE_GA/Enseignant/affiche.html",{"enseignant" : enseignant})


def update(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    form = EnseignantForm(enseignant.__dict__)
    return render(request,"SAE_GA/Enseignant/ajout.html",{"form" : form, "id" : id})

def updatetraitement(request, id):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        enseignant = lform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/SAE_GA/Enseignant/accueil")
    else :
        return render(request, "SAE_GA/Enseignant/ajout.html", {"form" : lform})


def delete(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/SAE_GA/Enseignant/accueil")