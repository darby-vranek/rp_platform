# Generated by Django 2.1.1 on 2019-03-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0004_auto_20190219_0121'),
        ('characters', '0011_auto_20190326_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactertrait',
            name='verse',
        ),
        migrations.AddField(
            model_name='charactertrait',
            name='verses',
            field=models.ManyToManyField(blank=True, null=True, related_name='character_traits', to='verses.Verse'),
        ),
    ]
