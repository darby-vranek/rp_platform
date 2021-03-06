# Generated by Django 3.0.2 on 2020-01-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_auto_20190517_0558'),
        ('verses', '0004_auto_20190219_0121'),
        ('notes', '0002_auto_20200119_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='characters',
            field=models.ManyToManyField(blank=True, to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='note',
            name='verses',
            field=models.ManyToManyField(blank=True, to='verses.Verse'),
        ),
    ]
