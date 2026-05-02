from django.db import models
from students.models import Student  # Cross-app import

class Project(models.Model):
    title = models.CharField(max_length=200)
    lead_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
