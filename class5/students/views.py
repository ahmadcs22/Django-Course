# students/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.db.models import Q # NEW: Imports advanced database querying


# 1. GET all students or POST a new student
@api_view(['GET', 'POST'])
def student_list_create(request):
    
    if request.method == 'GET':
        # 1. Check if React sent a 'search' parameter in the URL
        search_query = request.query_params.get('search', None)
        
        if search_query:
            # 2. Filter the database. 
            # `icontains` means "case-insensitive search".  
            # Q objects allow us to search multiple columns at once (First Name OR Roll Number)
            students = Student.objects.filter(
                Q(first_name__icontains=search_query) | 
                Q(roll_number__icontains=search_query)
            )
        else:
            # 3. If no search parameter, just return everyone
            students = Student.objects.all()
            
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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


