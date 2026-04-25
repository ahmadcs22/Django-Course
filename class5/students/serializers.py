from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'first_name', 'last_name', 'roll_number', 'email']
          # Or use '__all__' to automatically grab everything in the model!
        fields = '__all__'
