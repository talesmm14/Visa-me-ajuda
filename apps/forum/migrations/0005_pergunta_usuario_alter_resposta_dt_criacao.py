# Generated by Django 4.1.3 on 2022-11-13 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_alter_pergunta_dt_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='dt_criacao',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
