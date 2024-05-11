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
    status = forms.ChoiceField(
        choices = [('', '-----'),] + [(status.id, status.name) for status in Status.objects.all()] + [('add new', 'Add new')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Status'
    )

    class Meta:
        model = Contracts
        fields = '__all__'
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'client': forms.TextInput(attrs={'class': 'form-control'}),
        'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        labels = {
            'name': 'Contract name',
        }