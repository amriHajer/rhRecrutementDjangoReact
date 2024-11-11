from django.urls import path
from .views import (
    RhSignupView,
    EmployeSignupView,
    CandidatSignupView,
    CustomAuthToken,
    RhOnlyView,
    EmployeOnlyView,
    LogoutView,
    EmployeListView,
    EmployeDetail ,
    EmployeDeleteView ,
    CustomTokenObtainPairSerializer,
    CustomTokenObtainPairView,
)

from .permissions import IsRHUser, IsCandidatUser, IsEmployeUser
from . import views
urlpatterns = [
    path('signup/rh/', RhSignupView.as_view(), name='signup_rh'),
    path('signup/employe/', EmployeSignupView.as_view(), name='signup_employe'),
    path('signup/candidat/', CandidatSignupView.as_view(), name='signup_candidat'),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('rh/dashboard/', RhOnlyView.as_view(), name='rh-dashboard'),
    path('employe/dashboard/', EmployeOnlyView.as_view(), name='employe-dashboard'),
    path('candidat/dashboard/', EmployeOnlyView.as_view(), name='candidat-dashboard'),
    path('employes/', EmployeListView.as_view(), name='employe-list'),
    path('employes/<int:pk>/', EmployeDetail.as_view(), name='employe-detail'),
    path('api/employes/<int:pk>/', EmployeDeleteView.as_view(), name='employe-delete'),
    #*******
    path('leave-request/', views.leave_request, name='leave_request'),
    path('leave-list/', views.leave_list, name='leave_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]




