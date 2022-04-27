# Generated by Django 2.0 on 2022-04-23 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('earts', '0006_performance_file_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments_rating',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='comments_rating',
            name='STUDENT',
        ),
        migrations.RemoveField(
            model_name='comments_rating',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='comments_rating',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comments_rating',
            name='rating',
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]