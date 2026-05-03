from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=50)
    desc=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.roll_number} | {self.first_name} {self.last_name}"


