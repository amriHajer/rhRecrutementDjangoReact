from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Modèle personnalisé User
class User(AbstractUser):
    email = models.EmailField(unique=True) 
    is_rh = models.BooleanField(default=False)
    is_employe = models.BooleanField(default=False)
    is_candidat = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username

# Crée automatiquement un token d'authentification lorsque l'utilisateur est créé
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Modèle RH
class RH(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rh_profile")
    dateNaiss = models.DateField(null=True, blank=True)  # Champ pour la date de naissance

    def __str__(self):
        return f"RH: {self.user.username}"

# Modèle Employé
class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employe_profile")
    tel = models.CharField(max_length=15, blank=True, null=True)  # Ajout de null=True pour la base de données
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Employé: {self.user.username}"

# Modèle Candidat
class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidat_profile")
    tel = models.CharField(max_length=15, blank=True, null=True)  # Ajout de null=True pour la base de données

    def __str__(self):
        return f"Candidat: {self.user.username}"

from django.core.exceptions import ValidationError
from django.utils import timezone

from django.db import models
from datetime import timedelta

class Leave(models.Model):
    TYPE_CHOICES = [
        ('maladie', 'Congés maladie'),
        ('vacances', 'Congés vacances'),
        ('maternité', 'Congés maternité'),
        ('sabbatique', 'Congés sabbatique'),
    ]

    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('approuvee', 'Approuvée'),
        ('rejettee', 'Rejetée'),
    ]
    type_of_leave = models.CharField(max_length=50, choices=TYPE_CHOICES, default='maladie')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True, null=True, default='')
    
    approved_by = models.ForeignKey(RH, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    approval_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    comments = models.TextField(blank=True, null=True, default='')
    employee = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='leave_requests')

    def __str__(self):
        return f"{self.employee} - {self.get_type_of_leave_display()} du {self.start_date} au {self.end_date}"

    def get_type_of_leave_display(self):
        # Implémentez cette méthode si nécessaire
        return self.status

