# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-16 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_doc', models.CharField(max_length=255)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fic', models.CharField(blank=True, max_length=255, null=True)),
                ('url_fic', models.FileField(blank=True, null=True, upload_to='fichiers/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inform_actuel.Document')),
            ],
            options={
                'ordering': ['nom_fic'],
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adresse', models.CharField(blank=True, max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('telephone', models.CharField(blank=True, max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
