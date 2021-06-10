from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .decorators import unauthenticated_user
from .forms import *
from api.models import HardwareModel

@unauthenticated_user
def SigninView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontend:dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'user/signin.html', context)

@login_required(login_url='frontend:signin')
def LogoutView(request):
    logout(request)
    return redirect('frontend:dashboard')

@login_required(login_url='frontend:signin')
def DashboardView(request):
    context = {
        'hardwareStatusCount': [
            HardwareModel.objects.filter(status='Unassigned').count(),
            HardwareModel.objects.filter(status='To be delivered').count(),
            HardwareModel.objects.filter(status='Delivered').count(),
            HardwareModel.objects.filter(status='Returning').count(),
            HardwareModel.objects.filter(status='Returned').count(),
            HardwareModel.objects.filter(status='Kept').count()
        ]
    }
    return render(request, 'app/dashboard.html', context)

@login_required(login_url='frontend:signin')
def TesterView(request):
    form = TesterForm
    context = {
        'label': 'Tester',
        'form': form,
    }
    return render(request, 'app/tester.html', context)

@login_required(login_url='frontend:signin')
def CompanyView(request):
    form = CompanyForm
    context = {
        'label': 'Company',
        'form': form,
    }
    return render(request, 'app/company.html', context)

@login_required(login_url='frontend:signin')
def ProjectView(request):
    form = ProjectForm
    context = {
        'label': 'Project',
        'form': form,
    }
    return render(request, 'app/project.html', context)

@login_required(login_url='frontend:signin')
def HardwareView(request):
    form = HardwareForm
    context = {
        'label': 'Hardware',
        'form': form,
    }
    return render(request, 'app/hardware.html', context)

@login_required(login_url='frontend:signin')
def HardwareDetailsView(request, pk):
    hardware = get_object_or_404(HardwareModel, id=pk)
    data = {
        'name': hardware.name,
        'tester': hardware.tester,
        'project': hardware.project,
        'status': hardware.status,
        'notes': hardware.notes
    }
    form = HardwareForm(initial=data)
    context = {
        'object_id': hardware.id,
        'label': 'Hardware',
        'form': form,
    }
    return render(request, 'app/hardwareDetails.html', context)