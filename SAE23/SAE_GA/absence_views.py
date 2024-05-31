from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import AbsenceForm, CSVUploadForm
from . import models
from django.contrib import messages
import csv
from .models import Etudiant, Cours, Absence


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


def import_absences(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                etudiant_id = row['etudiant_id']
                cours_id = row['cours_id']
                justifie = row['justifie'].lower() == 'true'
                justification = row.get('justification', '')

                try:
                    etudiant = Etudiant.objects.get(id=etudiant_id)
                    cours = Cours.objects.get(id=cours_id)
                    absence = Absence.objects.create(
                        etudiant=etudiant,
                        cours=cours,
                        justifie=justifie,
                        justification=justification
                    )
                    absence = form.save()
                except Etudiant.DoesNotExist:
                    messages.error(request, f"Étudiant ID {etudiant_id} n'existe pas.")
                except Cours.DoesNotExist:
                    messages.error(request, f"Cours ID {cours_id} n'existe pas.")

            messages.success(request, "Absences importées avec succès.")
            return HttpResponseRedirect('/SAE_GA/Absence/accueil')
    else:
        form = CSVUploadForm()

    return render(request, 'SAE_GA/Absence/import.html', {'form': form})