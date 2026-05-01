from django.shortcuts import render


def student_data_g(request):
    
    return render(request, 'students/hello.html')
