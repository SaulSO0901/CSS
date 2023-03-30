# Generated by Django 4.1.7 on 2023-03-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Correo', models.CharField(max_length=200)),
                ('Telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Prestamo', models.DateTimeField()),
                ('Fecha_Devolucion', models.DateTimeField()),
                ('Equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.equipo')),
                ('Personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.personal')),
            ],
        ),
    ]
