# Generated by Django 2.1.1 on 2018-12-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faceclaim',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]