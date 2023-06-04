from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Tipo_Documento_Identidad, tipos_seguro, paciente, especialidades, doctores, citas_medicas, usuario

# Create your views here.
def home(request):
    return render(request, "home.html")

# USUARIOS
def list_user(request):
    user = request.user  # Obtener el usuario actual
    return render(request, 'app/perfil.html', {'user': user})


def update_user(request, username):
    user = usuario.objects.get(username=username)

    if request.method == 'POST':
        # Obtén los datos actualizados del formulario
        username = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        # Actualiza los campos del usuario
        user.username = username
        user.full_name = full_name
        user.email = email
        if password:
            user.set_password(password) 

        user.save()

        return redirect('/user/')  # Redirige a la página de perfil o a donde desees

    return render(request, 'app/update_perfil.html', {'user': user})



# DOCUMENTO DE IDENTIDAD
def list_document(request):
    documentos = Tipo_Documento_Identidad.objects.all()
    return render(request, 'app/documentoIdentidad.html', {'documentos':documentos})


def create_document(request):
    documento = Tipo_Documento_Identidad( tipo_documento_id=request.POST['tipo_documento_id'], tipo_documento_nombre=request.POST['tipo_documento_nombre'])
    documento.save()

    messages.success(request, 'El documento se ha creado exitosamente.')

    return redirect('/documentos/')


def update_document(request, id_documento):
    documento = Tipo_Documento_Identidad.objects.get(tipo_documento_id=id_documento)
    if request.method == 'POST':
        documento.tipo_documento_id = request.POST['tipo_documento_id']
        documento.tipo_documento_nombre = request.POST['tipo_documento_nombre']
        documento.save()
        
        messages.success(request, 'El documento se ha actualizado exitosamente.')

        return redirect('/documentos/')
    else:
        return render(request, 'app/update_document.html', {'documento': documento})


def delete_document(request, document_id):
    documentos = Tipo_Documento_Identidad.objects.get(tipo_documento_id=document_id)
    documentos.delete()
    messages.success(request, 'El documento se ha eliminado exitosamente.')

    return redirect('/documentos/')
# FIN DOCUMENTO DE IDENTIDAD


# TIPOS DE SEGURO
def list_seguro(request):
    seguros = tipos_seguro.objects.all()
    return render(request, 'app/tiposSeguro.html', {'seguros':seguros})

def create_seguro(request):
    seguros = tipos_seguro( tipo_seguro_id=request.POST['tipo_seguro_id'], tipo_seguro_nombre=request.POST['tipo_seguro_nombre'])
    seguros.save()
    messages.success(request, 'El seguro se ha creado exitosamente.')

    return redirect('/seguros/')

def update_seguro(request, seguro_id):
    seguro = tipos_seguro.objects.get(tipo_seguro_id=seguro_id)

    if request.method == 'POST':
        tipo_seguro_id = request.POST['tipo_seguro_id']
        tipo_seguro_nombre = request.POST['tipo_seguro_nombre']
        
        seguro.tipo_seguro_id = tipo_seguro_id
        seguro.tipo_seguro_nombre = tipo_seguro_nombre
        seguro.save()
        messages.success(request, 'El seguro se ha actualizado exitosamente.')
        
        return redirect('/seguros/') 
    
    return render(request, 'app/update_seguro.html', {'seguro': seguro})


def delete_seguro(request, seguro_id):
    seguros = tipos_seguro.objects.get(tipo_seguro_id=seguro_id)
    seguros.delete()
    messages.success(request, 'El seguro se ha eliminado exitosamente.')

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
    messages.success(request, 'El paciente se ha creado exitosamente.')

    return redirect('/pacientes/')


def update_paciente(request, paciente_id):
    pacientes = paciente.objects.get(id=paciente_id)
    
    if request.method == 'POST':
        tipo_documento_id = request.POST['tipo_documento_id']
        tipo_documento = Tipo_Documento_Identidad.objects.get(tipo_documento_id=tipo_documento_id)
        
        tipo_seguro_id = request.POST['tipo_seguro_id']
        tipo_seguros = tipos_seguro.objects.get(tipo_seguro_id=tipo_seguro_id)
        
        pacientes.tipo_documento_id = tipo_documento
        pacientes.nro_documento = request.POST['nro_documento']
        pacientes.nombre = request.POST['nombre']
        pacientes.apellidos = request.POST['apellidos']
        pacientes.direccion = request.POST['direccion']
        pacientes.fecha_nacimiento = request.POST['fecha_nacimiento']
        pacientes.tipo_seguro_id = tipo_seguros
        pacientes.save()
        messages.success(request, 'El paciente se ha actualizado exitosamente.')
        
        return redirect('/pacientes/') 
    
    tipos_documento = Tipo_Documento_Identidad.objects.all()
    tipos_seguros = tipos_seguro.objects.all()
    return render(request, 'app/update_pacientes.html', {'paciente': pacientes, 'tipos_documento': tipos_documento, 'tipos_seguros': tipos_seguros})


def delete_paciente(request, paciente_id):
    pacientes = paciente.objects.get(id=paciente_id)
    pacientes.delete()
    messages.success(request, 'El paciente se ha eliminado exitosamente.')

    return redirect('/pacientes/')
# FIN PACIENTES

# ESPECIALIDADES
def list_especialidades(request):
    especialidad = especialidades.objects.all()
    return render(request, 'app/especialidades.html', {'especialidades':especialidad})


def create_especialidad(request):
    especialidad = especialidades( especialidad_id=request.POST['especialidad_id'], especialidad_nombre=request.POST['especialidad_nombre'])
    especialidad.save()
    messages.success(request, 'La especialidad se ha creado exitosamente.')

    return redirect('/especialidades/')


def update_especialidad(request, especialidad_id):
    especialidad = especialidades.objects.get(especialidad_id=especialidad_id)
    
    if request.method == 'POST':
        especialidad.especialidad_id = request.POST['especialidad_id']
        especialidad.especialidad_nombre = request.POST['especialidad_nombre']
        especialidad.save()
        messages.success(request, 'La especialidad se ha actualizado exitosamente.')
        
        return redirect('/especialidades/')  # Redirigir a la lista de especialidades actualizada
    
    return render(request, 'app/update_especialidad.html', {'especialidad': especialidad})


def delete_especialidad(request, especialidad_id):
    especialidad = especialidades.objects.get(especialidad_id=especialidad_id)
    especialidad.delete()
    messages.success(request, 'La especialidad se ha eliminado exitosamente.')

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
    messages.success(request, 'El doctor se ha creado exitosamente.')

    return redirect('/doctores/')


def update_doctor(request, doctor_id):
    doctor = doctores.objects.get(doctor_id=doctor_id)
    
    if request.method == 'POST':
        doctor.doctor_id = request.POST['doctor_id']
        doctor.doctor_nombre = request.POST['doctor_nombre']
        doctor.doctor_direccion = request.POST['doctor_direccion']
        doctor.doctor_telefono = request.POST['doctor_telefono']
        doctor.save()
        messages.success(request, 'El doctor se ha actualizado exitosamente.')
        
        return redirect('/doctores/') 
    
    return render(request, 'app/update_doctores.html', {'doctor': doctor})


def delete_doctores(request, doctor_id):
    doctor = doctores.objects.get(doctor_id=doctor_id)
    doctor.delete()
    messages.success(request, 'El doctor se ha eliminado exitosamente.')

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
    messages.success(request, 'La cita se ha creado exitosamente.')

    return redirect('/citas/')


def update_citas(request, cita_id):
    cita = citas_medicas.objects.get(cita_id=cita_id)

    if request.method == 'POST':
        paciente_id = request.POST['paciente_id']
        paciente_obj = paciente.objects.get(id=paciente_id)
        
        especialidad_id = request.POST['especialidad_id']
        especialidad_obj = especialidades.objects.get(especialidad_id=especialidad_id)
        
        doctor_id = request.POST['doctor_id']
        doctor_obj = doctores.objects.get(doctor_id=doctor_id)
        
        username = request.POST['username']
        user_obj = usuario.objects.get(username=username)
        
        cita.cita_id = request.POST['cita_id']
        cita.observaciones = request.POST['observaciones']
        cita.fecha_cita = request.POST['fecha_cita']
        cita.doctor_id = doctor_obj
        cita.especialidad_id = especialidad_obj
        cita.paciente_id = paciente_obj
        cita.username_id = user_obj
        cita.save()
        messages.success(request, 'La cita se ha actualizado exitosamente.')
        
        return redirect('/citas/')  # Redirigir a la lista de citas actualizada

    pacientes = paciente.objects.all()
    especialidad = especialidades.objects.all()
    doctor = doctores.objects.all()
    usuarios = usuario.objects.all()
    return render(request, 'app/update_citas.html', {'cita': cita, 'pacientes': pacientes, 'especialidades': especialidad, 'doctores': doctor, 'usuarios': usuarios})


def delete_citas(request, cita_id):
    citas = citas_medicas.objects.get(cita_id=cita_id)
    citas.delete()
    messages.success(request, 'La cita se ha eliminado exitosamente.')

    return redirect('/citas/')
# FIN CITAS MEDICAS