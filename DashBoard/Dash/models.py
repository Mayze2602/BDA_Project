# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class StudentMentalHealth1(models.Model):
    student_timestamp = models.CharField(max_length=19, blank=True, null=True)
    gender = models.CharField(max_length=18, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    course = models.CharField(max_length=23, blank=True, null=True)
    student_year = models.CharField(max_length=26, blank=True, null=True)
    cgpa = models.CharField(max_length=18, blank=True, null=True)
    marital_status = models.CharField(max_length=14, blank=True, null=True)
    depression = models.CharField(max_length=23, blank=True, null=True)
    anxiety = models.CharField(max_length=20, blank=True, null=True)
    panic_attack = models.CharField(max_length=25, blank=True, null=True)
    treatment = models.CharField(max_length=44, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_mental_health_1'


class Studenthealth(models.Model):
    health_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    depression = models.IntegerField(blank=True, null=True)
    anxiety = models.IntegerField(blank=True, null=True)
    panic_attack = models.IntegerField(blank=True, null=True)
    treatment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studenthealth'


class Studentperformance(models.Model):
    performance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    student_year = models.IntegerField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentperformance'


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'

