from django.urls import path
from . import views

urlpatterns = [
    # The <int:student_id> captures the number in the URL and passes it to the view
    path('profile/<int:student_id>/', views.student_profile, name='student-profile'),
]
