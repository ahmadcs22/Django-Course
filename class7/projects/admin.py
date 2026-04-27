# students/admin.py
from django.contrib import admin

# 1. Import your model
from .models import Project

# 2. Register it with the admin site
admin.site.register(Project)
