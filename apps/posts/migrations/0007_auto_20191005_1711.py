# Generated by Django 2.1.1 on 2019-10-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]