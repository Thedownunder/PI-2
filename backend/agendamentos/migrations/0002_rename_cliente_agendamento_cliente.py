# Generated by Django 5.1.3 on 2024-11-24 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='Cliente',
            new_name='cliente',
        ),
    ]
