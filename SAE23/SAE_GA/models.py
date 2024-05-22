from django.db import models

# Create your models here.

class Cours(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField(blank=False, null = False)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE)
    duree=models.TimeField()
    groupe=models.ForeignKey("groupe", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Le cours {self.titre} ayant lieu le {self.date} dure {self.duree} et est enseigné par {self.enseignant}."
        return chaine
