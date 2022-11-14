# Generated by Django 4.1.3 on 2022-11-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0006_rename_iamgem_mapa_imagem_passo_imagem_trilha_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapa',
            name='ordem',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passo',
            name='links',
            field=models.ManyToManyField(blank=True, null=True, to='mapa.link'),
        ),
        migrations.AlterUniqueTogether(
            name='mapa',
            unique_together={('trilha', 'ordem')},
        ),
    ]
