# Generated by Django 5.1.3 on 2024-12-12 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_nome_disciplina_nome_disciplina_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turma',
            old_name='nome_turma',
            new_name='nome',
        ),
    ]