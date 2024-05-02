from rest_framework import serializers
from .models import Courses, Studenthealth, Studentperformance, Students


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['course_id', 'course_name']


class StudenthealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studenthealth
        fields = '__all__'


class StudentperformanceSerializer(serializers.ModelSerializer):
    # Define a nested serializer for the 'course' field
    course = CoursesSerializer()

    class Meta:
        model = Studentperformance
        fields = ['performance_id', 'student', 'course', 'student_year', 'cgpa']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'




