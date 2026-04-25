# students/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


# 1. GET all students or POST a new student
@api_view(['GET', 'POST'])
def student_list_create(request):
    
    if request.method == 'GET':
        students = Student.objects.all()
        # many=True tells the serializer we are sending a list of items, not just one.
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(): # <-- The Serializer checks for unique emails/roll numbers here!
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If invalid, DRF automatically creates a helpful error message for React
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. GET, PUT (Update), or DELETE a specific single student ok g
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)