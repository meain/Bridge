# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_sem', models.PositiveSmallIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3'), (4, 'S4'), (5, 'S5'), (6, 'S6'), (7, 'S7'), (8, 'S8')])),
                ('batch', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_code', models.CharField(max_length=3, verbose_name='Department Code')),
                ('dep_name', models.CharField(max_length=60, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.SmallIntegerField(verbose_name='Roll no.')),
                ('stud_name', models.CharField(max_length=40, verbose_name='Name')),
                ('current_sem', models.SmallIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3'), (4, 'S4'), (5, 'S5'), (6, 'S6'), (7, 'S7'), (8, 'S8')], null=True, verbose_name='Current Semester')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class', verbose_name='Class')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department', verbose_name='Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Subject Code')),
                ('subject_title', models.CharField(max_length=60, verbose_name='Subject Title')),
                ('subject_sem', models.SmallIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3'), (4, 'S4'), (5, 'S5'), (6, 'S6'), (7, 'S7'), (8, 'S8')], null=True)),
                ('subject_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department', verbose_name='Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=40)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department')),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subject', verbose_name='Subjects')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
    ]
