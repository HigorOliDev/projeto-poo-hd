# Generated by Django 5.1.2 on 2024-11-21 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_turma_ano_alter_professor_codigo_professor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
        ),
    ]
