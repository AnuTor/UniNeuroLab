# Generated by Django 2.2.17 on 2021-01-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTomaDatos', '0011_auto_20210120_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='adqdata_eeg_protocolo',
            name='eegData',
            field=models.CharField(max_length=50, null=True, verbose_name='Raw Signals'),
        ),
    ]