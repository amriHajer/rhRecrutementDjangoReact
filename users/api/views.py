#api/veiws.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import BasePermission
from .serializers import RhSignupSerializer, EmployeSignupSerializer, EmployeSerializer  , CandidatSignupSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .permissions import IsRHUser, IsEmployeUser, IsCandidatUser
from django.contrib.auth import authenticate
from users.models import User , Employe 
from .serializers import UserSerializer 


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


# Custom Auth Token View
# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'is_employe': user.is_employe,
#             'is_rh': user.is_rh,
#             'is_candidat': user.is_candidat,
#         })


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






class EmployeListView(APIView):
    def get(self, request):
        employes = Employe.objects.all()  # Obtenir tous les employés
        serializer = EmployeSerializer(employes, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeDetail(generics.RetrieveAPIView):
    queryset = Employe.objects.all()  # Obtenir un employé par ID
    serializer_class = EmployeSerializer
