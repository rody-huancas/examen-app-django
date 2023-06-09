# Generated by Django 4.2 on 2023-06-03 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_documento', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_documento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_documento_identidad')),
                ('tipo_seguro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipos_seguro')),
            ],
        ),
    ]
