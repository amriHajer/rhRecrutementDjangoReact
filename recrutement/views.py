from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from recrutement.models import OffreEmploi, Candidature
from recrutement.api.serializers import OffreEmploiSerializer, CandidatureSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class OffreEmploiViewSet(viewsets.ModelViewSet):
    """
    Cette vue permet de gérer les offres d'emploi.
    Elle inclut la possibilité d'afficher, créer, mettre à jour et supprimer des offres.
    """
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Cette méthode permet de créer une nouvelle offre d'emploi.
        Seul un utilisateur ayant les permissions appropriées (ex: RH) peut créer une offre.
        """
        if not request.user.is_authenticated:
            return Response({"detail": "Vous devez être connecté pour créer une offre."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Cette méthode permet de lister toutes les offres d'emploi.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CandidatureViewSet(viewsets.ModelViewSet):
    """
    Cette vue permet de gérer les candidatures pour les offres d'emploi.
    Elle inclut la possibilité d'afficher, créer, mettre à jour et supprimer des candidatures.
    """
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Cette méthode permet à un candidat de postuler à une offre d'emploi.
        On s'assure que le candidat peut soumettre une candidature.
        """
        # On associe l'utilisateur connecté à la candidature
        request.data['candidat'] = request.user.id
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Cette méthode permet de lister toutes les candidatures.
        """
        queryset = Candidature.objects.filter(candidat=request.user)  # Afficher uniquement les candidatures de l'utilisateur connecté
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Cette méthode permet de mettre à jour une candidature (par exemple, changement de statut).
        """
        candidature = self.get_object()
        if candidature.candidat != request.user:
            return Response({"detail": "Vous ne pouvez pas modifier cette candidature."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Cette méthode permet de supprimer une candidature.
        """
        candidature = self.get_object()
        if candidature.candidat != request.user:
            return Response({"detail": "Vous ne pouvez pas supprimer cette candidature."}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)
