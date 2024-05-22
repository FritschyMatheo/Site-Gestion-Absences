from django.db import models

# Create your models here.

class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"Nom: {self.nom}"
        return chaine
