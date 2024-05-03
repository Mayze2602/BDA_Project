from django.db.models import Count, Avg, Sum, Q
from django.shortcuts import render
import json

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
    # Consulta para condiciones de salud y tratamiento
    students_health = Studenthealth.objects.annotate(
        has_depression=Count('depression', filter=Q(depression__gt=0)),
        has_anxiety=Count('anxiety', filter=Q(anxiety__gt=0)),
        has_panic_attack=Count('panic_attack', filter=Q(panic_attack__gt=0)),
        receiving_treatment=Count('treatment', filter=Q(treatment__gt=0))
    )
    health_data = students_health.aggregate(
        total_with_depression=Sum('has_depression'),
        total_with_anxiety=Sum('has_anxiety'),
        total_with_panic_attack=Sum('has_panic_attack'),
        total_receiving_treatment=Sum('receiving_treatment')
    )
    health_data_json = json.dumps(health_data)
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
        'health_data': health_data_json
        
    }
    return render(request, 'Dash/dashboard.html',context)



