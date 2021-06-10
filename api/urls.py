from django.urls import path
from .views import *

urlpatterns = [
    path('tester/', TesterAPI.as_view(), name='TesterAPI'),
    path('tester/<int:pk>/', TesterAPI.as_view(), name='TesterAPI'),

    path('company/', CompanyAPI.as_view(), name='CompanyAPI'),
    path('company/<int:pk>/', CompanyAPI.as_view(), name='CompanyAPI'),

    path('project/', ProjectAPI.as_view(), name='ProjectAPI'),
    path('project/<int:pk>/', ProjectAPI.as_view(), name='ProjectAPI'),

    path('hardware/', HardwareAPI.as_view(), name='HardwareAPI'),
    path('hardware/<int:pk>/', HardwareAPI.as_view(), name='HardwareAPI'),
]
