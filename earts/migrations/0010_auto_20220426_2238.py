# Generated by Django 2.0 on 2022-04-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0009_auto_20220426_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='PROGRAM',
        ),
        migrations.DeleteModel(
            name='schedule',
        ),
    ]
