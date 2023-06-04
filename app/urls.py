from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import home, list_document, create_document, delete_document, list_seguro, create_seguro, delete_seguro, list_pacientes, create_paciente, delete_paciente, list_especialidades, create_especialidad, delete_especialidad, list_doctores, create_doctor, delete_doctores, list_citas, create_citas, delete_citas, update_document, update_seguro, update_paciente, update_especialidad, update_doctor, update_citas

urlpatterns = [
    path("", home, name="home"),
    # documentos
    path("documentos/", list_document, name="documentos"),
    path("documentos/crear/", create_document, name="documentos_crear"),
    path('update_document/<int:id_documento>/', update_document, name='update_document'),
    path('delete_document/<int:document_id>/', delete_document, name='delete_document'),
    # seguro
    path("seguros/", list_seguro, name="seguros"),
    path("seguros/crear/", create_seguro, name="seguros_crear"),
    path('update_seguros/<int:seguro_id>/', update_seguro, name='update_seguro'),
    path("delete_seguro/<int:seguro_id>/", delete_seguro, name="delete_seguro"),
    # Pacientes
    path("pacientes/", list_pacientes, name="pacientes"),
    path("pacientes/crear/", create_paciente, name="pacientes_crear"),
    path('update_paciente/<int:paciente_id>/', update_paciente, name='update_paciente'),
    path("delete_paciente/<int:paciente_id>/", delete_paciente, name="delete_paciente"),
    # Especialidades
    path("especialidades/", list_especialidades, name="especialidades"),
    path("especialidades/crear/", create_especialidad, name="especialidades_crear"),
    path('update_especialidad/<int:especialidad_id>/', update_especialidad, name='update_especialidad'),
    path("delete_especialidades/<int:especialidad_id>/", delete_especialidad, name="delete_especialidad"),
    # Doctores
    path("doctores/", list_doctores, name="doctores"),
    path("doctores/crear/", create_doctor, name="doctores_crear"),
    path('update_doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path("delete_doctores/<int:doctor_id>/", delete_doctores, name="delete_doctores"),
    # Citas medicas
    path("citas/", list_citas, name="citas"),
    path("citas/crear/", create_citas, name="citas_crear"),
    path("citas_actualizar/<int:cita_id>/", update_citas, name="citas_actualizar"),
    path("citas/<int:cita_id>/", delete_citas, name="delete_citas"),
]