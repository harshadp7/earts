# Generated by Django 2.0 on 2022-04-21 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0002_performance_totalscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='totalscore',
        ),
    ]
