from django.shortcuts import render
from .models import Project

def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': all_projects})
