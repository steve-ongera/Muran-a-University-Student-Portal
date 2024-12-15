# Generated by Django 5.0 on 2024-03-23 08:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_code', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=100)),
                ('lec', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=100)),
                ('disability', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('medical', models.CharField(max_length=100)),
                ('co_curricular', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.units')),
            ],
        ),
    ]
