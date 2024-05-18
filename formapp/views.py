from django.shortcuts import render, redirect, get_object_or_404
from .forms import StatusForm, ContractsForm
from .models import Status, Contracts


def index(request): 
    contracts = Contracts.objects.all()
    contracts_form = ContractsForm()  
    status_form = StatusForm()
    statuses = Status.objects.all()
    context = {
        'contracts': contracts,
        'contracts_form': contracts_form,
        'status_form': status_form,
        'statuses': statuses,
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


def delete_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return redirect('index')