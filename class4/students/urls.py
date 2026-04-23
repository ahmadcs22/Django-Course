# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Example URL: /api/students/
    path('api/students/', views.student_list_create, name='student-list-create'),
    
    # Example URL: /api/students/5/
    path('api/students/<int:pk>/', views.student_detail, name='student-detail'),
]