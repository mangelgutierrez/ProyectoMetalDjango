# Generated by Django 4.1 on 2022-09-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMetal', '0003_rename_bandas_grupos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupos',
            old_name='anio_fundacion',
            new_name='fundacion',
        ),
    ]
