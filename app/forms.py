from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tipo_Documento_Identidad, tipos_seguro


class DocumentoIdentidad(forms.Form):
    nroDocumento = forms.CharField(
        label="Número de Documento",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el número de documento"}),
    )
    nombreDocumento = forms.CharField(
        label="Nombre de Documento",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el nombre de documento"}),
    )
