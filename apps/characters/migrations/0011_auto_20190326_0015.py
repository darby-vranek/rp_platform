# Generated by Django 2.1.1 on 2019-03-26 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20190325_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactertrait',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='charactertrait',
            name='verse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='character_traits', to='verses.Verse'),
        ),
    ]
