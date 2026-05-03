# students/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# 1. Serve the Basic Frontend
def frontend_view(request):
    return render(request, 'index.html')

# 2. CREATE (POST) and READ (GET) Students
@api_view(['GET', 'POST'])
def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# 3. DELETE a Student
@api_view(['DELETE'])
def student_delete_api(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({"message": "Student deleted successfully"})
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
