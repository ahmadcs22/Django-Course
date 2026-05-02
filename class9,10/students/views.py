from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student



@login_required(login_url='/accounts/login/')
def student_profile(request, student_id):
    # Fetch the specific student using their ID
    student = Student.objects.get(id=student_id)
    
    return render(request, 'students/profile.html', {'student': student})


