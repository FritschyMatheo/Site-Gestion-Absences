from django.shortcuts import render, HttpResponseRedirect
from .forms import GroupeForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = GroupeForm(request)
        return render(request, "SAE_GA/Groupe/ajout.html", {"form" : form})
    else :
        form = GroupeForm()
        return render(request, "SAE_GA/Groupe/ajout.html", {"form" : form})


def traitement(request):
    lform = GroupeForm(request.POST)
    if lform.is_valid():
        groupe = lform.save()
        return HttpResponseRedirect("/SAE_GA/Groupe/accueil")
    else :
        return render(request, "SAE_GA/Groupe/ajout.html", {"form" : lform})


def accueil(request):
    liste = list(models.Groupe.objects.all())
    return render(request,"SAE_GA/Groupe/accueil.html", {"liste": liste})

def affiche(request, id):
    groupe = models.Groupe.objects.get(pk=id)
    return render(request, "SAE_GA/Groupe/affiche.html", {"groupe": groupe})

def update(request, id):
    groupe = models.Groupe.objects.get(pk=id)
    form = GroupeForm(groupe.__dict__)
    return render(request,"SAE_GA/Groupe/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    lform = GroupeForm(request.POST)
    if lform.is_valid():
        groupe = lform.save(commit = False)
        groupe.id = id
        groupe.save()
        return HttpResponseRedirect("/SAE_GA/Groupe/accueil")
    else :
        return render(request, "SAE_GA/Groupe/ajout.html", {"form" : lform})


def delete(request, id):
    groupe = models.Groupe.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/SAE_GA/Groupe/accueil")