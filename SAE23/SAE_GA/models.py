from django.db import models

# Create your models here.

class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"Nom : {self.nom}"
        return chaine

class Cours(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField(blank=False, null = False)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE)
    duree=models.TimeField()
    groupe=models.ForeignKey("groupe", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Le cours {self.titre} ayant lieu le {self.date} dure {self.duree} et est enseigné par {self.enseignant}."
        return chaine


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        chaine = f"Nom : {self.nom}, Prénom : {self.prenom}, Email: {self.email}"
        return chaine