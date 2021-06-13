from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView, name='signin'),
    path('logout/', LogoutView, name="logout"),
    path('dashboard/', DashboardView, name='dashboard'),
    path('tester/', TesterView, name='tester'),
    path('tester/<int:pk>', TesterDetailsView, name="testerDetails"),
    path('company/', CompanyView, name='company'),
    path('company/<int:pk>', CompanyDetailsView, name="companyDetails"),
    path('project/', ProjectView, name='project'),
    path('project/<int:pk>', ProjectDetailsView, name="projectDetails"),
    path('hardware/', HardwareView, name='hardware'),
    path('hardware/<int:pk>', HardwareDetailsView, name="hardwareDetails"),
]
