from rest_framework import generics
from recrutement.models import Candidature, OffreEmploi
from .serializers import CandidatureSerializer, OffreEmploiSerializer
from rest_framework.permissions import IsAuthenticated

# Vues pour les offres d'emploi (pour afficher toutes les offres et les détails d'une offre)
class OffreEmploiListCreateAPIView(generics.ListCreateAPIView):
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiSerializer
    #permission_classes = [IsAuthenticated]  # Permet seulement aux utilisateurs connectés d'accéder

class OffreEmploiRetrieveAPIView(generics.RetrieveAPIView):
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiSerializer
    lookup_field = 'pk'

# Vues pour les candidatures (création, mise à jour, suppression, liste)
class CandidatureListCreateAPIView(generics.ListCreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associe automatiquement la candidature au candidat connecté
        serializer.save(candidat=self.request.user)

class CandidatureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        # Restreint la suppression et mise à jour aux candidats propriétaires
        return self.queryset.filter(candidat=self.request.user)
