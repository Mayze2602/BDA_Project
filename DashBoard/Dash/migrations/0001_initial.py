# Generated by Django 5.0.4 on 2024-05-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Studenthealth',
            fields=[
                ('health_id', models.AutoField(primary_key=True, serialize=False)),
                ('depression', models.IntegerField(blank=True, null=True)),
                ('anxiety', models.IntegerField(blank=True, null=True)),
                ('panic_attack', models.IntegerField(blank=True, null=True)),
                ('treatment', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'studenthealth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Studentperformance',
            fields=[
                ('performance_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_year', models.IntegerField(blank=True, null=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'studentperformance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
    ]
