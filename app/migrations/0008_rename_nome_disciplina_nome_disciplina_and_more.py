# Generated by Django 5.1.3 on 2024-12-08 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_turma_horario_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='nome',
            new_name='nome_disciplina',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='nome',
            new_name='turma',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='nome',
            new_name='nome_turma',
        ),
    ]