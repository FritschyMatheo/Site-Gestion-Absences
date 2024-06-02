import csv
from django.shortcuts import render, HttpResponseRedirect
from .forms import AbsenceForm, CSVUploadForm
from . import models
from django.contrib import messages
from .forms import CSVUploadForm
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
            try:
                # Try reading the file with UTF-8 encoding first
                decoded_file = csv_file.read().decode('utf-8').splitlines()
            except UnicodeDecodeError:
                # If there's an error, try with ISO-8859-1 encoding
                csv_file.seek(0)  # Reset file pointer
                decoded_file = csv_file.read().decode('iso-8859-1').splitlines()

            reader = csv.DictReader(decoded_file)

            # Check if the expected columns exist in the CSV
            expected_columns = ['etudiant_id', 'cours_id', 'accepte', 'justification']
            if not all(column in reader.fieldnames for column in expected_columns):
                messages.error(request, "Le fichier CSV doit contenir les colonnes 'etudiant_id', 'cours_id', 'accepte', 'justification'.")
                return render(request, 'SAE_GA/Absence/import.html', {'form': form})

            for row in reader:
                etudiant_id = row.get('etudiant_id')
                cours_id = row.get('cours_id')
                accepte = row.get('accepte', '').lower() == 'true'
                justification = row.get('justification', '')

                if not etudiant_id or not cours_id:
                    messages.error(request, "Les identifiants 'etudiant_id' et 'cours_id' sont requis.")
                    continue

                try:
                    etudiant = Etudiant.objects.get(id=etudiant_id)
                    cours = Cours.objects.get(id=cours_id)
                    Absence.objects.create(
                        etudiant=etudiant,
                        cours=cours,
                        accepte=accepte,
                        justification=justification
                    )
                except Etudiant.DoesNotExist:
                    messages.error(request, f"Étudiant ID {etudiant_id} n'existe pas.")
                except Cours.DoesNotExist:
                    messages.error(request, f"Cours ID {cours_id} n'existe pas.")

            messages.success(request, "Absences importées avec succès.")
            return HttpResponseRedirect('/SAE_GA/Absence/accueil')
    else:
        form = CSVUploadForm()

    return render(request, 'SAE_GA/Absence/import.html', {'form': form})

    return render(request, 'SAE_GA/Absence/import.html', {'form': form})