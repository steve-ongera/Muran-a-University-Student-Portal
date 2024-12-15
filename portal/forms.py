# student/forms.py
from django import forms
from .models import Registration, Units

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].widget = forms.CheckboxSelectMultiple()

        # Query available units and populate choices dynamically
        self.fields['unit'].queryset = Units.objects.all()
