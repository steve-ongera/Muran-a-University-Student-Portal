# Generated by Django 5.0 on 2024-03-23 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_unitcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='unitCode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.unitcode'),
            preserve_default=False,
        ),
    ]
