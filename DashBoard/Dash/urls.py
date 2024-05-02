from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='Home'),
    path('students/', views.students, name='Students'),
    path('courses/', views.courses, name='Courses'),
    path('studenthealth/', views.studenthealth, name='Studenthealth'),
    path('studentperformance/', views.studentperformance, name='Studentperformance')
]