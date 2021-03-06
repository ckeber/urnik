# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smer', models.CharField(max_length=192)),
                ('leto', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'letniki',
                'ordering': ('smer', 'leto'),
                'default_related_name': 'letniki',
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=192)),
                ('priimek', models.CharField(max_length=192)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('domaca_stran', models.CharField(blank=True, max_length=192)),
            ],
            options={
                'verbose_name_plural': 'osebe',
                'ordering': ('priimek', 'ime'),
                'default_related_name': 'osebe',
            },
        ),
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=192)),
                ('kratica', models.CharField(max_length=64)),
                ('stevilo_studentov', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('letniki', models.ManyToManyField(blank=True, related_name='predmeti', to='urnik.Letnik')),
                ('slusatelji', models.ManyToManyField(blank=True, related_name='predmeti', to='urnik.Oseba')),
            ],
            options={
                'verbose_name_plural': 'predmeti',
                'ordering': ('ime',),
                'default_related_name': 'predmeti',
            },
        ),
        migrations.CreateModel(
            name='Srecanje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(blank=True, choices=[('P', 'predavanja'), ('S', 'seminar'), ('V', 'vaje'), ('L', 'laboratorijske vaje')], max_length=1)),
                ('oznaka', models.CharField(blank=True, max_length=64)),
                ('dan', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ponedeljek'), (2, 'torek'), (3, 'sreda'), (4, 'četrtek'), (5, 'petek')], null=True)),
                ('ura', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('trajanje', models.PositiveSmallIntegerField(null=True)),
                ('predmet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='srecanja', to='urnik.Predmet')),
            ],
            options={
                'verbose_name_plural': 'srečanja',
                'ordering': ('predmet', 'tip', 'oznaka', 'ucitelj', 'dan', 'ura', 'trajanje'),
                'default_related_name': 'srecanja',
            },
        ),
        migrations.CreateModel(
            name='Ucilnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(blank=True, choices=[('M', 'matematična'), ('F', 'fizikalna'), ('R', 'računalniška'), ('P', 'praktikum'), ('K', 'pisarna'), ('X', 'zunanja')], default='X', max_length=1)),
                ('oznaka', models.CharField(max_length=192, unique=True)),
                ('velikost', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ucilnice',
                'ordering': ('oznaka',),
                'default_related_name': 'ucilnice',
            },
        ),
        migrations.AddField(
            model_name='srecanje',
            name='ucilnica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srecanja', to='urnik.Ucilnica'),
        ),
        migrations.AddField(
            model_name='srecanje',
            name='ucitelj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srecanja', to='urnik.Oseba'),
        ),
    ]
