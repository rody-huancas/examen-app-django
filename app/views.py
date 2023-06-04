from django.shortcuts import render, redirect
from .models import Tipo_Documento_Identidad, tipos_seguro, paciente, especialidades

# Create your views here.
def home(request):
    return render(request, "home.html")

# DOCUMENTO DE IDENTIDAD
def list_document(request):
    documentos = Tipo_Documento_Identidad.objects.all()
    return render(request, 'app/documentoIdentidad.html', {'documentos':documentos})

def create_document(request):
    documento = Tipo_Documento_Identidad( tipo_documento_id=request.POST['tipo_documento_id'], tipo_documento_nombre=request.POST['tipo_documento_nombre'])
    documento.save()
    return redirect('/documentos/')


def delete_document(request, document_id):
    documentos = Tipo_Documento_Identidad.objects.get(tipo_documento_id=document_id)
    documentos.delete()
    return redirect('/documentos/')
# FIN DOCUMENTO DE IDENTIDAD


# TIPOS DE SEGURO
def list_seguro(request):
    seguros = tipos_seguro.objects.all()
    return render(request, 'app/tiposSeguro.html', {'seguros':seguros})

def create_seguro(request):
    seguros = tipos_seguro( tipo_seguro_id=request.POST['tipo_seguro_id'], tipo_seguro_nombre=request.POST['tipo_seguro_nombre'])
    seguros.save()
    return redirect('/seguros/')

def delete_seguro(request, seguro_id):
    seguros = tipos_seguro.objects.get(tipo_seguro_id=seguro_id)
    seguros.delete()
    return redirect('/seguros/')
# FIN TIPOS DE SEGURO

# PACIENTES
def list_pacientes(request):
    pacientes = paciente.objects.all()
    tipos_documento = Tipo_Documento_Identidad.objects.all()
    tipos_seguros = tipos_seguro.objects.all()
    return render(request, 'app/pacientes.html', {'pacientes': pacientes, 'tipos_documento': tipos_documento, 'tipos_seguros': tipos_seguros})


def create_paciente(request):
    tipo_documento_id = request.POST['tipo_documento_id']
    tipo_documento = Tipo_Documento_Identidad.objects.get(tipo_documento_id=tipo_documento_id)
    
    tipo_seguro_id = request.POST['tipo_seguro_id']
    tipo_seguro = tipos_seguro.objects.get(tipo_seguro_id=tipo_seguro_id)
    
    pacientes = paciente(
        tipo_documento_id=tipo_documento,
        nombre=request.POST['nombre'],
        apellidos=request.POST['apellidos'],
        direccion=request.POST['direccion'],
        fecha_nacimiento=request.POST['fecha_nacimiento'],
        tipo_seguro_id=tipo_seguro
    )
    
    pacientes.save()
    return redirect('/pacientes/')



def delete_paciente(request, paciente_id):
    pacientes = paciente.objects.get(id=paciente_id)
    pacientes.delete()
    return redirect('/pacientes/')
# FIN PACIENTES

# ESPECIALIDADES
def list_especialidades(request):
    especialidad = especialidades.objects.all()
    return render(request, 'app/especialidades.html', {'especialidades':especialidad})

# FIN ESPECIALIDADES
