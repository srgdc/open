from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from openapp.models import *
from openapp.forms import *

def home(request):
    projects = Project.objects.all()
    return render(request, "openapp/home.html", {"projects": projects})

def search(request):
    language = request.GET['language']
    name = request.GET['name']
    code_crumbs = Code.objects.filter(language__name__exact = language, name__contains = name).order_by('-rating')
    projects = Project.objects.filter(language__name__exact = language, name__contains = name).order_by('-rating')
    return render(request, "openapp/search.html", {"code_crumbs": code_crumbs, "projects": projects})

def code(request, code_id):
    return render(request, "openapp/code.html", {"code": get_object_or_404(Code, id=code_id)})

def project(request, pid):
    return render(request, "openapp/project.html", {"project": get_object_or_404(Project, id=pid)})

@login_required
def submit(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            object = project_form.save()
            object.users.add(request.user.id)
            object.save()
            return redirect(object)
        return render(request, "openapp/submit.html", {"form": project_form})
    else:
        return render(request, "openapp/submit.html", {"form": ProjectForm()})