# Generated by Django 5.0.1 on 2024-02-28 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_cursoestudiantes_curso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_servicio', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanico')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo')),
            ],
        ),
    ]