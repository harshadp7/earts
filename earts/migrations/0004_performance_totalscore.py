# Generated by Django 2.0 on 2022-04-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0003_remove_performance_totalscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='totalscore',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
