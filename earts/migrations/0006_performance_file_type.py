# Generated by Django 2.0 on 2022-04-23 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0005_auto_20220423_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='file_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]