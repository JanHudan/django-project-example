from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView, name='signin'),
    path('logout/', LogoutView, name="logout"),
    path('dashboard/', DashboardView, name='dashboard'),
    path('tester/', TesterView, name='tester'),
    path('company/', CompanyView, name='company'),
    path('project/', ProjectView, name='project'),
    path('hardware/', HardwareView, name='hardware'),
    path('hardware/<int:pk>', HardwareDetailsView, name="hardwareDetails"),
]
