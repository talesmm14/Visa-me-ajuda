# Generated by Django 4.1.3 on 2022-11-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, unique=True, verbose_name='Titulo')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PerguntaEResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=120, unique=True, verbose_name='Pergunta')),
                ('resposta', models.TextField(verbose_name='Respota')),
            ],
        ),
        migrations.CreateModel(
            name='Passo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, verbose_name='Titulo')),
                ('descricao', models.TextField()),
                ('mapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa.mapa')),
            ],
        ),
    ]
