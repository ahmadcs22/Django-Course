from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_data_g, name='student_data_g'),
]
