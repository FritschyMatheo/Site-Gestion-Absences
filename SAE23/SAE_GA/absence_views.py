from django.shortcuts import render, HttpResponseRedirect
from .forms import AbsenceForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = AbsenceForm(request)
        return render(request, "SAE_GA/Absence/ajout.html", {"form" : form, "id": None})
    else :
        form = AbsenceForm()
        return render(request, "SAE_GA/Absence/ajout.html", {"form" : form})


def traitement(request):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        absence = lform.save()
        return HttpResponseRedirect("/SAE_GA/Absence/accueil")
    else :
        return render(request, "SAE_GA/Absence/ajout.html", {"form" : lform})

def accueil(request):
    liste = list(models.Absence.objects.all())
    return render(request,"SAE_GA/Absence/accueil.html", {"liste": liste})

def affiche(request, id):
    absence = models.Absence.objects.get(pk=id)
    return render(request, "SAE_GA/Absence/affiche.html", {"absence": absence})


def update(request, id):
    absence = models.Absence.objects.get(pk=id)
    form = AbsenceForm(absence.__dict__)
    return render(request,"SAE_GA/Absence/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        absence = lform.save(commit = False)
        absence.id = id
        absence.save()
        return HttpResponseRedirect("/SAE_GA/Absence/accueil")
    else :
        return render(request, "SAE_GA/Absence/ajout.html", {"form" : lform, "id": id})

def delete(request, id):
    absence = models.Absence.objects.get(pk=id)
    absence.delete()
    return HttpResponseRedirect("/SAE_GA/Absence/accueil")