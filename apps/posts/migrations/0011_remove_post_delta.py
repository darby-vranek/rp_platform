# Generated by Django 2.1.1 on 2019-10-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_delta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='delta',
        ),
    ]
