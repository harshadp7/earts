# Generated by Django 2.0 on 2022-04-25 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0007_auto_20220424_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='program_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
