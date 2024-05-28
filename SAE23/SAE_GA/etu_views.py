from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import EtudiantForm
from . import models


def ajout(request):
    if request.method == "POST":
        form = EtudiantForm(request)
        return render(request,"SAE_GA/Etudiant/ajout.html", {"form" : form, "id": None})
    else :
        form = EtudiantForm()
        return render(request,"SAE_GA/Etudiant/ajout.html", {"form" : form})

def traitement(request):
    lform = EtudiantForm(request.POST, request.FILES)
    if lform.is_valid():
        etudiant = lform.save()
        return HttpResponseRedirect("/SAE_GA/Etudiant/accueil")
    else :
        return render(request, "SAE_GA/Etudiant/ajout.html", {"form" : lform})

def accueil(request):
    liste = list(models.Etudiant.objects.all())
    return render(request,"SAE_GA/Etudiant/accueil.html",{"liste" : liste})

def affiche(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    return render(request,"SAE_GA/Etudiant/affiche.html",{"etudiant" : etudiant})


def update(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('SAE_GA/Etudiant/accueil.html')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request,"SAE_GA/Etudiant/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    lform = EtudiantForm(request.POST, request.FILES)
    if lform.is_valid():
        etudiant = lform.save(commit = False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/SAE_GA/Etudiant/accueil")
    else :
        return render(request, "SAE_GA/Etudiant/ajout.html", {"form" : lform, "id": id})

def delete(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/SAE_GA/Etudiant/accueil")