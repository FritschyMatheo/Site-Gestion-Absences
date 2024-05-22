from django.shortcuts import render, HttpResponseRedirect
from .forms import CoursForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = CoursForm(request)
        if form.is_valid():
            Cours = form.save()
            return render(request,"SAE_GA/Cours/affiche.html",{"Cours" : Cours})
        else:
            return render(request,"SAE_GA/Cours/ajout.html",{"form": form})
    else :
        form = CoursForm()
        return render(request,"SAE_GA/Cours/ajout.html",{"form" : form})

def traitement(request):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        cours = lform.save()
        return render(request, "SAE_GA/Cours/affiche.html", {"cours" : cours})
    else:
        return render(request, "SAE_GA/Cours/ajout.html", {"form" : lform})
    
def affiche(request, id):
    Cours = models.Cours.objects.get(pk=id)
    return render(request,"SAE_GA/Cours/ajout.html",{"Cours": Cours})

def update(request, id):
    cours = models.Cours.objects.get( pk = id)
    form = CoursForm(cours.__dict__)
    return render(request, "SAE_GA/Cours/ajout.html", {"form" : form, "id": id})