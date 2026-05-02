from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project

# Adding this single line locks the view down!
@login_required(login_url='/accounts/login/')
def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': all_projects})
