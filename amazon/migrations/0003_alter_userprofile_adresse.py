# Generated by Django 4.1.9 on 2023-06-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0002_alter_userprofile_adresse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adresse',
            field=models.CharField(max_length=255, verbose_name='adresse'),
        ),
    ]
