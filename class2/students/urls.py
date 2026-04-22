from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend_view, name='frontend'), # The visual page
    path('api/students/', views.student_list_api, name='student-api'), # GET/POST data
    path('api/students/<int:pk>/', views.student_delete_api, name='student-delete'), # DELETE data
]


