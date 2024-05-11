from django.shortcuts import render, redirect
from .forms import StatusForm, ContractsForm
from .models import Status, Contracts


def index(request): 
    contracts = Contracts.objects.all()
    contracts_form = ContractsForm()  
    status_form = StatusForm()
    context = {
        'contracts': contracts,
        'contracts_form': contracts_form,
        'status_form': status_form,
    }
    return render(request, 'formapp/index.html', context)

def contracts_create(request):
    if request.method == 'POST':
        form = ContractsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')

def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')