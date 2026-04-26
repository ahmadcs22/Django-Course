from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)

        if search_query:
            return Student.objects.filter(
                Q(first_name__icontains=search_query) |
                Q(roll_number__icontains=search_query)
            )
        
        return Student.objects.all()