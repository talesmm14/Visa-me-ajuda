# Generated by Django 4.1.3 on 2022-11-13 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0002_passo_ordem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='passo',
            unique_together={('mapa', 'ordem')},
        ),
    ]
