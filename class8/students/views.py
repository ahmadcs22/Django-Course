from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def student_data_g(request):
    
    return render(request, 'students/hello.html')
