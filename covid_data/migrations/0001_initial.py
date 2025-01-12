# Generated by Django 3.0.5 on 2020-04-22 17:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('geometria', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('geometria_simplificada', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('geometria_web', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
                ('geometria_web_simplificada', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
                ('centroide', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('centroide_web', django.contrib.gis.db.models.fields.PointField(srid=3857)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.CharField(max_length=3, unique=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('codigo', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=31)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=63)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('clave', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('clave_municipio', models.IntegerField()),
                ('geometria', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('geometria_simplificada', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('geometria_web', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
                ('geometria_web_simplificada', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
                ('centroide', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('centroide_web', django.contrib.gis.db.models.fields.PointField(srid=3857)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid_data.Entidad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_el', models.DateTimeField(auto_now_add=True)),
                ('renglon', models.IntegerField(help_text='Renglón en la tabla liberada más reciente.')),
                ('id_registro', models.CharField(help_text='Identificador en la tabla liberada más reciente.', max_length=80)),
                ('fecha_actualizacion', models.DateField(help_text='La base de datos se alimenta diariamente, esta variable permite identificar la fecha de la ultima actualizacion.', null=True)),
                ('fecha_ingreso', models.DateField(help_text='Identifica la fecha de ingreso del paciente a la unidad de atención.', null=True)),
                ('fecha_sintomas', models.DateField(help_text='Idenitifica la fecha en que inició la sintomatología del paciente.', null=True)),
                ('fecha_defuncion', models.DateField(help_text='Identifica la fecha en que el paciente falleció.', null=True)),
                ('edad', models.IntegerField(help_text='Identifica la edad del paciente.')),
                ('asma', models.ForeignKey(help_text='Identifica si el paciente tiene un diagnóstico de asma.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='asma', to='covid_data.SiNo')),
                ('cardiovascular', models.ForeignKey(help_text='Identifica si el paciente tiene un diagnóstico de enfermedades cardiovasculares.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cardiovascular', to='covid_data.SiNo')),
                ('diabetes', models.ForeignKey(help_text='Identifica si el paciente tiene un diagnóstico de diabetes.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diabetes', to='covid_data.SiNo')),
                ('embarazo', models.ForeignKey(help_text='Identifica si la paciente está embarazada.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='embarazo', to='covid_data.SiNo')),
                ('entidad_nacimiento', models.ForeignKey(help_text='Identifica la entidad de nacimiento del paciente.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entidad_nacimiento', to='covid_data.Entidad')),
                ('entidad_residencia', models.ForeignKey(help_text='Identifica la entidad de residencia del paciente.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entidad_residencia', to='covid_data.Entidad')),
                ('entidad_um', models.ForeignKey(help_text='Identifica la entidad donde se ubica la unidad medica que brindó la atención.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entidad_um', to='covid_data.Entidad')),
                ('epoc', models.ForeignKey(help_text='Identifica si el paciente tiene un diagnóstico de EPOC.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='epoc', to='covid_data.SiNo')),
                ('habla_lengua_indigena', models.ForeignKey(help_text='Identifica si el paciente habla lengua índigena.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='habla_lengua_indigena', to='covid_data.SiNo')),
                ('hipertension', models.ForeignKey(help_text='Identifica si el paciente tiene un diagnóstico de hipertensión.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hipertension', to='covid_data.SiNo')),
                ('inmusupr', models.ForeignKey(help_text='Identifica si el paciente presenta inmunosupresión.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inmusupr', to='covid_data.SiNo')),
                ('intubado', models.ForeignKey(help_text='Identifica si el paciente requirió de intubación.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='intubado', to='covid_data.SiNo')),
                ('migrante', models.ForeignKey(help_text='Identifica si el paciente es una persona migrante.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='migrante', to='covid_data.SiNo')),
                ('municipio_residencia', models.ForeignKey(help_text='Identifica el municipio de residencia del paciente.', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Municipio')),
                ('nacionalidad', models.ForeignKey(help_text='Identifica si el paciente es mexicano o extranjero.', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Nacionalidad')),
                ('neumonia', models.ForeignKey(help_text='Identifica si al paciente se le diagnosticó con neumonía.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='neumonia', to='covid_data.SiNo')),
                ('obesidad', models.ForeignKey(help_text='Identifica si el paciente tiene diagnóstico de obesidad.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='obesidad', to='covid_data.SiNo')),
                ('origen', models.ForeignKey(help_text='La vigilancia centinela se realiza a través del sistema de unidades de salud monitoras de enfermedades respiratorias (USMER). Las USMER incluyen unidades médicas del primer, segundo o tercer nivel de atención y también participan como USMER las unidades de tercer nivel que por sus características contribuyen a ampliar el panorama de información epidemiológica, entre ellas las que cuenten con especialidad de neumología, infectología o pediatría. (Categorías en Catalógo Anexo).', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Origen')),
                ('otras_com', models.ForeignKey(help_text='Identifica si el paciente tiene diagnóstico de otras enfermedades.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='otras_com', to='covid_data.SiNo')),
                ('otro_caso', models.ForeignKey(help_text='Identifica si el paciente tuvo contacto con algún otro caso diagnósticado con SARS CoV-2', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='otro_caso', to='covid_data.SiNo')),
                ('pais_nacionalidad', models.ForeignKey(help_text='Identifica la nacionalidad del paciente.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pais_nacionalidad', to='covid_data.Pais')),
                ('pais_origen', models.ForeignKey(help_text='Identifica el país del que partió el paciente rumbo a México.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pais_origen', to='covid_data.Pais')),
                ('renal_cronica', models.ForeignKey(help_text='Identifica si el paciente tiene diagnóstico de insuficiencia renal crónica.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='renal_cronica', to='covid_data.SiNo')),
                ('resultado', models.ForeignKey(help_text='Identifica el resultado del análisis de la muestra reportado por el  laboratorio de la Red Nacional de Laboratorios de Vigilancia Epidemiológica (INDRE, LESP y LAVE). (Catálogo de resultados diagnósticos anexo).', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Resultado')),
                ('sector', models.ForeignKey(help_text='Identifica el tipo de institución del Sistema Nacional de Salud que brindó la atención.', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Sector')),
                ('sexo', models.ForeignKey(help_text='Identifica al sexo del paciente.', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.Sexo')),
                ('tabaquismo', models.ForeignKey(help_text='Identifica si el paciente tiene hábito de tabaquismo.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tabaquismo', to='covid_data.SiNo')),
                ('tipo_paciente', models.ForeignKey(help_text='Identifica el tipo de atención que recibió el paciente en la unidad. Se denomina como ambulatorio si regresó a su casa o se denomina como hospitalizado si fue ingresado a hospitalización.', null=True, on_delete=django.db.models.deletion.PROTECT, to='covid_data.TipoPaciente')),
                ('uci', models.ForeignKey(help_text='Identifica si el paciente requirió ingresar a una Unidad de Cuidados Intensivos.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uci', to='covid_data.SiNo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
