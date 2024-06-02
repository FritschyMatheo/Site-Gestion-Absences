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
            csv_file = request.FILES['csv_file'] # Récupétation du fichier CSV
            try:
                # Lecture du fichier avec l'encodage UTF-8
                decoded_file = csv_file.read().decode('utf-8').splitlines()
            except UnicodeDecodeError:
                # S'il y a une erreur, lecture avec ISO-8859-1
                csv_file.seek(0) # Réinitialise le pointeur du fichier
                decoded_file = csv_file.read().decode('iso-8859-1').splitlines()

            reader = csv.DictReader(decoded_file) # Crée un lecteur CSV qui interprète les lignes comme dans un dictionnaire

            # Cherche les colonnes du fichier CSV des absences
            expected_columns = ['etudiant_id', 'cours_id', 'accepte', 'justification']
            if not all(column in reader.fieldnames for column in expected_columns):
                messages.error(request, "Le fichier CSV doit contenir les colonnes 'etudiant_id', 'cours_id', 'accepte', 'justification'.")
                return render(request, 'SAE_GA/Absence/import.html', {'form': form})

            for row in reader:
                # Récupération des valeurs de chaque attribut
                etudiant_id = row.get('etudiant_id')
                cours_id = row.get('cours_id')
                accepte = row.get('accepte', '').lower() == 'true'
                justification = row.get('justification', '')

                if not etudiant_id or not cours_id:
                    # Vérifie les identifiants
                    messages.error(request, "Les identifiants 'etudiant_id' et 'cours_id' sont requis.")
                    continue # Passe à la ligne suivante du CSV

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