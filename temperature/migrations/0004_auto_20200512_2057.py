# Generated by Django 3.0.5 on 2020-05-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_mediciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediciones',
            name='codigos',
            field=models.CharField(max_length=25, verbose_name='Codigos'),
        ),
        migrations.AlterField(
            model_name='mediciones',
            name='observacion',
            field=models.CharField(max_length=30, verbose_name='Observacion'),
        ),
    ]
