from django.shortcuts import render, redirect
from .models import Tipo_Documento_Identidad, tipos_seguro, paciente, especialidades, doctores, citas_medicas, usuario

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
        nro_documento=request.POST['nro_documento'],
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


def create_especialidad(request):
    especialidad = especialidades( especialidad_id=request.POST['especialidad_id'], especialidad_nombre=request.POST['especialidad_nombre'])
    especialidad.save()
    return redirect('/especialidades/')


def delete_especialidad(request, especialidad_id):
    especialidad = especialidades.objects.get(especialidad_id=especialidad_id)
    especialidad.delete()
    return redirect('/especialidades/')
# FIN ESPECIALIDADES

# DOCTORES
def list_doctores(request):
    doctor = doctores.objects.all()
    return render(request, 'app/doctores.html', {'doctores':doctor})


def create_doctor(request):
    doctor = doctores( doctor_id=request.POST['doctor_id'], 
                      doctor_nombre=request.POST['doctor_nombre'],
                      doctor_direccion=request.POST['doctor_direccion'],
                      doctor_telefono=request.POST['doctor_telefono'])
    doctor.save()
    return redirect('/doctores/')


def delete_doctores(request, doctor_id):
    doctor = doctores.objects.get(doctor_id=doctor_id)
    doctor.delete()
    return redirect('/doctores/')
# FIN DOCTORES

# CITAS MEDICAS
def list_citas(request):
    citas = citas_medicas.objects.all()
    pacientes = paciente.objects.all()
    especialidad = especialidades.objects.all()
    doctor = doctores.objects.all()
    user = usuario.objects.all()
    
    return render(request, 'app/citasMedicas.html', {'citas': citas ,'pacientes': pacientes, 'especialidad': especialidad, 'doctor': doctor, 'user': user})


def create_citas(request):
    paciente_id = request.POST['paciente_id']
    paciente_obj = paciente.objects.get(id=paciente_id)
    
    especialidad_id = request.POST['especialidad_id']
    especialidad_obj = especialidades.objects.get(especialidad_id=especialidad_id)
    
    doctor_id = request.POST['doctor_id']
    doctor_obj = doctores.objects.get(doctor_id=doctor_id)
    
    username = request.POST['username']
    user_obj = usuario.objects.get(username=username)
    
    cita = citas_medicas(
        cita_id=request.POST['cita_id'],
        observaciones=request.POST['observaciones'],
        fecha_cita=request.POST['fecha_cita'],
        doctor_id=doctor_obj,
        especialidad_id=especialidad_obj,
        paciente_id=paciente_obj,
        username_id=user_obj
    )
    
    cita.save()
    return redirect('/citas/')


def delete_citas(request, cita_id):
    citas = citas_medicas.objects.get(cita_id=cita_id)
    citas.delete()
    return redirect('/citas/')
# FIN CITAS MEDICAS