# Generated by Django 4.0.3 on 2022-03-15 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='centre_examen',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='Candidat',
        ),
        migrations.DeleteModel(
            name='Centre',
        ),
    ]
