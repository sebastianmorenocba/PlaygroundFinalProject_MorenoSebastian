# Generated by Django 5.0.1 on 2024-02-08 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_profesor_mecanico'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Cliente',
        ),
    ]