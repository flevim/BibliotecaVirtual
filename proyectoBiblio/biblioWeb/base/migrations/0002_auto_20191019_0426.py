# Generated by Django 2.2.6 on 2019-10-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AddField(
            model_name='document',
            name='is_guide_document',
            field=models.BooleanField(default=False, verbose_name='Documento de Pauta'),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(max_length=255, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='document',
            name='level',
            field=models.CharField(choices=[('KINDER', 'Kinder'), ('PRIMERO', '1ero Básico'), ('SEGUNDO', '2do Básico'), ('TERCERO', '3ero Básico'), ('CUARTO', '4to Básico'), ('QUINTO', '5to Básico'), ('SEXTO', '6to Básico'), ('SEPTIMO', '7mo Básico'), ('OCTAVO', '8vo Básico'), ('PRIMERO_MEDIO', '1ero Medio'), ('SEGUNDO_MEDIO', '2do Medio'), ('TERCERO_MEDIO', '3ero Medio'), ('CUARTO_MEDIO', '4to Médio')], max_length=13),
        ),
    ]
