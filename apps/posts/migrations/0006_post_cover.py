# Generated by Django 2.1.1 on 2019-08-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190317_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.URLField(blank=True, default=''),
        ),
    ]