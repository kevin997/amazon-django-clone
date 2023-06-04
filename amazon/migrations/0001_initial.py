# Generated by Django 4.1.9 on 2023-06-04 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('adresse', models.CharField(max_length=255, verbose_name='adresse')),
                ('date_naissance', models.DateTimeField(max_length=100, null=True, verbose_name='date_naissance')),
                ('lieu_naissance', models.CharField(max_length=100, null=True, verbose_name='lieu_naissance')),
                ('pays_residence', models.CharField(max_length=100, null=True, verbose_name='pays_residence')),
                ('photo', models.TextField(null=True, verbose_name='photo')),
                ('type_piece_identite', models.CharField(max_length=255, null=True, verbose_name='type_piece_identite')),
                ('numero_piece_identite', models.CharField(max_length=255, null=True, verbose_name='numero_piece_identite')),
                ('date_expiration_piece_identite', models.CharField(max_length=255, null=True, verbose_name='numero_piece_identite')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserProfiles',
            },
        ),
    ]