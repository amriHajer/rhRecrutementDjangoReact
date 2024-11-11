from django.db import models
from users.models import User  


class OffreEmploi(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    entreprise = models.CharField(max_length=255)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return self.titre


class Candidature(models.Model):
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)
    offre = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE)
    date_candidature = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    name = models.CharField(max_length=255)  # Nouveau champ pour le nom
    telephone = models.CharField(max_length=20)  # Nouveau champ pour le numéro de téléphone

    def __str__(self):
        return f"{self.candidat} - {self.offre.titre}"
