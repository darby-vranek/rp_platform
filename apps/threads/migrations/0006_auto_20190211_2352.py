# Generated by Django 2.1.1 on 2019-02-11 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0005_auto_20190127_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['created'], 'verbose_name_plural': 'Replies'},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-created']},
        ),
    ]
