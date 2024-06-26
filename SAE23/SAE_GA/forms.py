from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre', 'date', 'enseignant', 'duree', 'groupe')
        labels={
            'titre' : _('Titre du cours'),
            'date' : _('Date'),
            'enseignant' : _('Enseignant'),
            'duree' : _('Durée'),
            'groupe' : _('Groupe')
        }
        
class GroupeForm(ModelForm):
        class Meta:
            model = models.Groupe
            fields = ('nom',)
            labels = {
            'nom' : _('Nom'),
            }


class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nom', 'prenom', 'email')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom'),
            'email' : _('Email')
        }

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom', 'prenom', 'email', 'groupe', 'photo')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom'),
            'email' : _('Email'),
            'groupe' : _('Groupe'),
            'photo' : _('Photo')
        }

class AbsenceForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = ('etudiant', 'cours', 'accepte', 'justification')
        labels = {
            'etudiant' : _('Etudiant'),
            'cours' : _('Cours'),
            'accepte' : _('L\'absence est-elle acceptée :'),
            'justification' : _('Justification')
        }

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Sélectionnez un fichier CSV")