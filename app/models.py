from django.db import models
from users.models import usuario

# Create your models here.
class Tipo_Documento_Identidad(models.Model):
    tipo_documento_id = models.CharField(max_length=25, primary_key=True)
    tipo_documento_nombre=models.CharField(max_length=150, null=False)

    REQUIRED_FIELD = ["tipo_documento_nombre"]

    class Meta:
        db_table = "Tipo_Documento_Identidad"


class tipos_seguro(models.Model):
    tipo_seguro_id = models.CharField(max_length=25, primary_key=True)
    tipo_seguro_nombre=models.CharField(max_length=150, null=False)

    REQUIRED_FIELD = ["tipo_seguro_nombre"]

    class Meta:
        db_table = "tipos_seguro"


class paciente(models.Model):
    tipo_documento_id=models.ForeignKey(Tipo_Documento_Identidad, on_delete=models.CASCADE)
    nro_documento=models.CharField(max_length=10, null=False)
    nombre=models.CharField(max_length=100, null=False)
    apellidos=models.CharField(max_length=100, null=False)
    direccion=models.CharField(max_length=100, null=False)
    fecha_nacimiento=models.DateField()
    tipo_seguro_id=models.ForeignKey(tipos_seguro, on_delete=models.CASCADE)


class especialidades(models.Model):
    especialidad_id = models.CharField(max_length=25, primary_key=True)
    especialidad_nombre=models.CharField(max_length=100, null=False)

class doctores(models.Model):
    doctor_id = models.CharField(max_length=25, primary_key=True)
    doctor_nombre = models.CharField(max_length=100, null=False)
    doctor_direccion = models.CharField(max_length=100, null=False)
    doctor_telefono = models.CharField(max_length=12, null=False)


class citas_medicas(models.Model):
    cita_id = models.CharField(max_length=25, primary_key=True)
    paciente_id = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    especialidad_id = models.ForeignKey(especialidades, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctores, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=250, null=False)
    username = models.ForeignKey(usuario, on_delete=models.CASCADE)



