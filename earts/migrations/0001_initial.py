# Generated by Django 2.0 on 2021-11-21 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comments_rating',
            },
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=50)),
                ('reply', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('deptartment', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.CharField(max_length=50)),
                ('event_discription', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='judges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'judges',
            },
        ),
        migrations.CreateModel(
            name='judges_assigned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EVENTS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.events')),
                ('JUDGES', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.judges')),
            ],
            options={
                'db_table': 'judges_assigned',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'participants',
            },
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance_name', models.CharField(max_length=50)),
                ('uploaded_files', models.CharField(max_length=500)),
                ('PARTICIPANTS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.participants')),
            ],
            options={
                'db_table': 'performance',
            },
        ),
        migrations.CreateModel(
            name='program_committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.CharField(max_length=50)),
                ('EVENTS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.events')),
            ],
            options={
                'db_table': 'program_committee',
            },
        ),
        migrations.CreateModel(
            name='programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=50)),
                ('program_discription', models.CharField(max_length=50)),
                ('EVENTS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.events')),
            ],
            options={
                'db_table': 'programs',
            },
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('result1', models.CharField(max_length=50)),
                ('result2', models.CharField(max_length=50)),
                ('result3', models.CharField(max_length=50)),
                ('PROGRAMS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.programs')),
            ],
            options={
                'db_table': 'result',
            },
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.programs')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.login')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('COURSE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.course')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.login')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='subadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subadmin_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.login')),
            ],
            options={
                'db_table': 'subadmin',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.student'),
        ),
        migrations.AddField(
            model_name='program_committee',
            name='STAFF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.staff'),
        ),
        migrations.AddField(
            model_name='performance',
            name='PROGRAMS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.programs'),
        ),
        migrations.AddField(
            model_name='participants',
            name='PROGRAMS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.programs'),
        ),
        migrations.AddField(
            model_name='participants',
            name='STUDENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.student'),
        ),
        migrations.AddField(
            model_name='judges_assigned',
            name='PROGRAMS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.programs'),
        ),
        migrations.AddField(
            model_name='judges',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.login'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='JUDGES',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earts.judges'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='STUDENT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='earts.student'),
        ),
        migrations.AddField(
            model_name='comments_rating',
            name='STUDENT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='earts.student'),
        ),
    ]
