from django.db.models import Count, Avg, Sum
from django.shortcuts import render

from .models import Courses, Studentperformance, Studenthealth, Students


# Create your views here.
def dashboard(request):
    total_students = Studentperformance.objects.all().count()
    total_courses = Courses.objects.all().count()
    average_gpa = Studentperformance.objects.aggregate(Avg('cgpa'))['cgpa__avg']
    context = {
        'total_courses': total_courses,
        'total_students': total_students,
        'average_gpa': average_gpa,
    }
    return render(request, 'Dash/dashboard.html',context)


def students(request):
    total_students = Students.objects.all().count()
    age_average = Students.objects.aggregate(Avg('age'))['age__avg']
    context = {
        'total_students': total_students,
        'age_average': age_average,
    }
    return render(request, 'Dash/students.html',context)


def studenthealth(request):
    # Obtener el número de estudiantes con depresión
    students_depression = Studenthealth.objects.filter(depression=True).count()

    # Obtener el número de estudiantes con ansiedad
    students_anxiety = Studenthealth.objects.filter(anxiety=True).count()

    # Obtener el número total de ataques de pánico
    number_panic_attacks = Studenthealth.objects.filter(panic_attack__gt=0).count()

    context = {
        'Students_Depression': students_depression,
        'Students_Anxiety': students_anxiety,
        'number_panic_attacks': number_panic_attacks,
    }

    return render(request, 'Dash/student_health.html', context)




def courses(request):
    total_courses = Courses.objects.all().count()

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

    context = {
        'total_courses': total_courses,
        'course_most': course_most_name,
        'course_most_people': course_most_people,
        'course_best_gpa': course_best_gpa_name,
        'course_best_gpa_avg': course_best_gpa_avg,
    }
    return render(request, 'Dash/courses.html', context)



def studentperformance(request):
    average_gpa = Studentperformance.objects.aggregate(avg_cgpa=Avg('cgpa'))['avg_cgpa']
    average_student_year = Studentperformance.objects.aggregate(avg_student_year=Avg('student_year'))['avg_student_year']
    context = {
        'average_gpa': average_gpa,
        'average_student_year': average_student_year,
    }
    return render(request, 'Dash/student_performance.html', context)



