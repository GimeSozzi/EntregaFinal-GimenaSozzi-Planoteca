# Generated by Django 4.2 on 2023-04-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyectos', '0002_proyecto_planos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='planos',
            field=models.FileField(blank=True, null=True, upload_to='planos'),
        ),
    ]