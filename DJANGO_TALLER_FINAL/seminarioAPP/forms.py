from django import forms
from seminarioAPP.models import seminario, institucion
from django.core import validators

class FormProyecto(forms.ModelForm):
    class Meta:
        model = seminario
        fields = '__all__'



