# Generated by Django 2.1.1 on 2019-04-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0005_auto_20190412_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='icons',
            field=models.ManyToManyField(related_name='collections', to='icons.Icon'),
        ),
    ]
