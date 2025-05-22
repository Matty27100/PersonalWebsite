from django.shortcuts import render
from .models import Project, Activity

# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    # Use the ordering from the model's Meta class
    activities = Activity.objects.all()
    return render(request, 'project/home.html', {
        'projects': projects,
        'activities': activities
    })

def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'project/project_detail.html', {'project': project})
