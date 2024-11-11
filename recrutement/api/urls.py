from django.urls import path
from .views import (
    OffreEmploiListCreateAPIView,
    OffreEmploiRetrieveAPIView,
    CandidatureListCreateAPIView,
    CandidatureRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('offres/', OffreEmploiListCreateAPIView.as_view(), name='offre-emploi-list-create'),
    path('offre/<int:pk>/', OffreEmploiRetrieveAPIView.as_view(), name='offre-emploi-detail'),


    path('candidatures/', CandidatureListCreateAPIView.as_view(), name='candidature-list-create'),
    path('candidature/<int:pk>/', CandidatureRetrieveUpdateDestroyAPIView.as_view(), name='candidature-detail-update-delete'),
]
