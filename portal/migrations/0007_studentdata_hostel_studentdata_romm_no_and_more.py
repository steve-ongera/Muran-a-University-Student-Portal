# Generated by Django 5.0 on 2024-03-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_studentdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='hostel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='romm_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
