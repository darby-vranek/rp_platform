# Generated by Django 2.1.1 on 2019-01-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20190127_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
