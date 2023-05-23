# Generated by Django 4.2 on 2023-05-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyectos', '0004_alter_proyecto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tipologia',
            field=models.CharField(blank=True, choices=[('vivienda unifamiliar', 'Vivienda Unifamiliar'), ('vivienda colectiva', 'Vivienda Colectiva'), ('duplex', 'Duplex'), ('edificio residencial', 'Edificio Residencial'), ('edificio comercial ', 'Edificio Comercial'), ('edificio oficinal', 'Edificio Oficinas')], default='other', max_length=30, null=True),
        ),
    ]