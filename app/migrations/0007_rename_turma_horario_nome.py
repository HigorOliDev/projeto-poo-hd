# Generated by Django 5.1.3 on 2024-12-08 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_turma_disciplinas_turma_sala_delete_notas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='turma',
            new_name='nome',
        ),
    ]
