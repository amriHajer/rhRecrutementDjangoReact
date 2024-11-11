#api/veiws.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import BasePermission
from .serializers import RhSignupSerializer, EmployeSignupSerializer, EmployeSerializer  , CandidatSignupSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404, redirect, render
from .permissions import IsRHUser, IsEmployeUser, IsCandidatUser
from django.contrib.auth import authenticate
from users.models import User , Employe 
from .serializers import UserSerializer 
from rest_framework.permissions import IsAuthenticated

# Permissions Classes
class IsRHUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_rh)


class IsEmployeUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employe)


class IsCandidatUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_candidat)


# Signup Views
class RhSignupView(generics.CreateAPIView):
    serializer_class = RhSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response({
            'user': user_data['user'],
            'refresh': user_data['refresh'],
            'access': user_data['access'],
        }, status=status.HTTP_201_CREATED)


class EmployeSignupView(generics.CreateAPIView):
    serializer_class = EmployeSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response({
            'user': user_data['user'],
            'refresh': user_data['refresh'],
            'access': user_data['access'],
        }, status=status.HTTP_201_CREATED)


class CandidatSignupView(generics.CreateAPIView):
    serializer_class = CandidatSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response({
            'user': user_data['user'],
            'refresh': user_data['refresh'],
            'access': user_data['access'],
        }, status=status.HTTP_201_CREATED)


class CustomAuthToken(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Veuillez fournir un email et un mot de passe.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authentifier l'utilisateur par email
        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({'error': 'Identifiants invalides.'}, status=status.HTTP_400_BAD_REQUEST)

        # Récupérer ou créer un token pour l'utilisateur
        token, created = Token.objects.get_or_create(user=user)
        return Response({
           'token': token.key,
            'user_id': user.pk,
            'is_employe': user.is_employe,
            'is_rh': user.is_rh,
            'is_candidat': user.is_candidat,
        })



#****************************************
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token payload
        token['is_rh'] = user.is_rh
        token['is_employe'] = user.is_employe
        token['is_candidat'] = user.is_candidat

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add the user's roles to the response data
        data['user'] = {
            'is_rh': self.user.is_rh,
            'is_employe': self.user.is_employe,
            'is_candidat': self.user.is_candidat,
        }

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#****************************************
# Logout View
class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


# Role-based views
class RhOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsRHUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class EmployeOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsEmployeUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CandidatOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsCandidatUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user





#***************************************
class EmployeListView(APIView):
    def get(self, request):
        employes = Employe.objects.all()  # Obtenir tous les employés
        serializer = EmployeSerializer(employes, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeDetail(generics.RetrieveAPIView):
    queryset = Employe.objects.all()  # Obtenir un employé par ID
    serializer_class = EmployeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework import status
from users.models import Leave, Employe
from .serializers import LeaveSerializer, LeaveRequestSerializer  # Create these serializers

@api_view(['POST'])
def leave_request(request):
    if request.method == 'POST':
        serializer = LeaveRequestSerializer(data=request.data)
        if serializer.is_valid():
            leave_request = serializer.save(employee=Employe.objects.get(user=request.user))
            return Response({"message": "Leave request submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def leave_list(request):
    leaves = Leave.objects.select_related('employee', 'approved_by').all()
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeListView(APIView):
    def get(self, request):
        employes = Employe.objects.all()  # Obtenir tous les employés
        serializer = EmployeSerializer(employes, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeDetail(generics.RetrieveAPIView):
    queryset = Employe.objects.all()  # Obtenir un employé par ID
    serializer_class = EmployeSerializer




#*********************
class EmployeDeleteView(generics.DestroyAPIView):
    queryset = Employe.objects.all()
    permission_classes = [IsAuthenticated]  # Vérifie si l'utilisateur est authentifié
    serializer_class = EmployeSerializer

    def delete(self, request, *args, **kwargs):
        try:
            employe = self.get_object()  # Récupère l'employé à supprimer
            employe.user.delete()  # Supprime l'utilisateur associé
            return Response(status=status.HTTP_204_NO_CONTENT)  # Retourne un statut 204 (No Content) si réussi
        except Employe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            



#****************************
