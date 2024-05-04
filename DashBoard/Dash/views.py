from django.db.models import Count, Avg, Sum, Q
from django.shortcuts import render
import json
from collections import Counter
import numpy as np

from .models import Courses, Studentperformance, Studenthealth, Students


# Create your views here.
def dashboard(request):
        #Total de estudiantes
    total_students = Studentperformance.objects.all().count()
        #Total de cursos
    total_courses = Courses.objects.all().count()
        #Promedio de GPA
    average_gpa = Studentperformance.objects.aggregate(Avg('cgpa'))['cgpa__avg']
        # Obtener el número de estudiantes con depresión
    students_depression = Studenthealth.objects.filter(depression=True).count()
        # Obtener el número de estudiantes con ansiedad
    students_anxiety = Studenthealth.objects.filter(anxiety=True).count()
        # Obtener el número total de ataques de pánico
    number_panic_attacks = Studenthealth.objects.filter(panic_attack__gt=0).count()
        # Promedio de edad de los estudiantes
    age_average = Students.objects.aggregate(Avg('age'))['age__avg']
        # Promedio de año de los estudiantes
    average_student_year = Studentperformance.objects.aggregate(avg_student_year=Avg('student_year'))['avg_student_year']
    # Curso con el mayor número de estudiantes
    course_most = Studentperformance.objects.values('course__course_name').annotate(
        total_students=Count('student')).order_by('-total_students').first()
    course_most_name = course_most['course__course_name']
    course_most_people = course_most['total_students']
    # Curso con el mejor GPA
    course_best_gpa = Studentperformance.objects.values('course__course_name').annotate(
        avg_cgpa=Avg('cgpa')).order_by('-avg_cgpa').first()
    course_best_gpa_name = course_best_gpa['course__course_name']
    course_best_gpa_avg = course_best_gpa['avg_cgpa']
        # Obtener el número de estudiantes por curso para tabla de cursos
    students_per_course = Studentperformance.objects.values('course__course_name').annotate(
        total_students=Count('student')).order_by('course__course_name')
    courses = [student['course__course_name'] for student in students_per_course]
    students = [student['total_students'] for student in students_per_course]
    courses_json = json.dumps(courses)
    students_json = json.dumps(students)

    health_conditions = {
        'anxiety': Studenthealth.objects.filter(anxiety__gt=0).count(),
        'depression': Studenthealth.objects.filter(depression__gt=0).count(),
        'panic_attacks': Studenthealth.objects.filter(panic_attack__gt=0).count()
    }
    condition_counts_json = json.dumps(health_conditions)

    # Obtener estudiantes por género
    gender_counts = Students.objects.values('gender').annotate(count=Count('student_id')).order_by('gender')
    gender_counts_dict = {entry['gender']: entry['count'] for entry in gender_counts if entry['gender']}
    gender_counts_json = json.dumps(gender_counts_dict)

     # Obtener la distribución de edades
    age_distribution = Students.objects.values('age').annotate(count=Count('age')).order_by('age')
    ages = [entry['age'] for entry in age_distribution]
    age_counts = [entry['count'] for entry in age_distribution]
    ages_json = json.dumps(ages)
    age_counts_json = json.dumps(age_counts)

    # Obtener la distribución del estado civil
    marital_distribution = Students.objects.values('marital_status').annotate(count=Count('marital_status')).order_by('marital_status')
    marital_statuses = [entry['marital_status'] for entry in marital_distribution]
    marital_counts = [entry['count'] for entry in marital_distribution]
    marital_statuses_json = json.dumps(marital_statuses)
    marital_counts_json = json.dumps(marital_counts)

    # Data for Average CGPA by Course Bar Chart
    avg_cgpa_per_course = Studentperformance.objects.values('course__course_name').annotate(avg_cgpa=Avg('cgpa')).order_by('course__course_name')
    courses = [entry['course__course_name'] for entry in avg_cgpa_per_course]
    avg_cgpas = [float(entry['avg_cgpa']) for entry in avg_cgpa_per_course]
    courses_json = json.dumps(courses)
    avg_cgpas_json = json.dumps(avg_cgpas)

    # Collecting CGPA data
    cgpas = list(Studentperformance.objects.values_list('cgpa', flat=True).filter(cgpa__isnull=False))

    # Define bins for histogram
    bins = np.arange(2.0, 4.2, 0.2)  # This creates bins from 2.0 to 4.0 in increments of 0.1
    hist, bin_edges = np.histogram(cgpas, bins=bins)

    # Convert the histogram data and bins for JSON serialization
    hist_json = json.dumps(hist.tolist())
    bins_json = json.dumps(bin_edges.tolist())



    context = {
        'total_courses': total_courses,
        'total_students': total_students,
        'average_gpa': average_gpa,
        'courses': courses_json,
        'students': students_json,
        'age_average': age_average,
        'students_depression': students_depression,
        'students_anxiety': students_anxiety,
        'number_panic_attacks': number_panic_attacks,
        'average_student_year': average_student_year,
        'course_most': course_most_name,
        'course_most_people': course_most_people,
        'course_best_gpa': course_best_gpa_name,
        'course_best_gpa_avg': course_best_gpa_avg,
        'condition_counts': condition_counts_json,
        'gender_counts': gender_counts_json,
        'ages': ages_json,
        'age_counts': age_counts_json,
        'marital_statuses': marital_statuses_json,
        'marital_counts': marital_counts_json,
        'courses': courses_json,
        'avg_cgpas': avg_cgpas_json,
        'hist': hist_json,
        'bins': bins_json,
        
    }
    return render(request, 'Dash/dashboard.html',context)



