from django import forms
from .models import Status, Contracts


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'disabled': 'disabled'}),
        }


class ContractsForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super(ContractsForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = [('', '-----'),] + [(status.id, status.name) for status in Status.objects.filter(active=True)] + [('add new', 'Add new'),]

    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'client': forms.TextInput(attrs={'class': 'form-control'}),
        'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'status': forms.Select(attrs={'class': 'form-select'}),
        }

        labels = {
            'name': 'Contract name',
        }