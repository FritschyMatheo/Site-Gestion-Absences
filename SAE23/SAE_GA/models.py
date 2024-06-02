from django.db import models

# Create your models here.

class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

class Cours(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField(blank=False, null = False)
    #enseignant=models.CharField(max_length=100)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE)
    duree=models.TimeField()
    #groupe=models.CharField(max_length=100)
    groupe=models.ForeignKey("groupe", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.titre}"
        return chaine

class Absence(models.Model):
    #etudiant=models.CharField(max_length=100)
    etudiant=models.ForeignKey("etudiant", on_delete=models.CASCADE, default=None)
    #cours=models.CharField(max_length=100)
    cours=models.ForeignKey("cours", on_delete=models.CASCADE, default=None)
    accepte=models.BooleanField()
    justification=models.TextField(null = True, blank = False)

    def __str__(self):
        if self.accepte == True:
            chaine = f"Absence de {self.etudiant}  au cours de {self.cours}. Absence acceptée."
        else :
            chaine = f"Absence de {self.etudiant}  au cours de {self.cours}. Absence refusée car justification non valable : {self.justification}"
        return chaine

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        chaine = f"{self.nom.upper()} {self.prenom}"
        return chaine


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    #groupe = models.CharField(max_length=100)
    groupe = models.ForeignKey("groupe", on_delete=models.CASCADE, default=None)
    photo = models.ImageField(null=True)
    def __str__(self):
        chaine = f"{self.nom.upper()} {self.prenom}"
        return chaine