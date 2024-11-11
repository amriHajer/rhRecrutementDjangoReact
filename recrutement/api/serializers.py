from rest_framework import serializers
from recrutement.models import Candidature, OffreEmploi

# Serializer pour la Candidature
class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = ['id', 'offre', 'candidat', 'date_candidature', 'cv', 'name', 'telephone']

# Serializer pour l'OffreEmploi
class OffreEmploiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffreEmploi
        fields = ['id', 'titre', 'description', 'date_publication', 'date_expiration', 'entreprise', 'salaire', 'localisation']
