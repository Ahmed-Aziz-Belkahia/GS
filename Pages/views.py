from django.shortcuts import render

from Pages.models import Service, Project

# Create your views here.

def index0(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST.get("fullname"))
    services = Service.objects.all()
    projects = Project.objects.all()
    return render(request, "runok/index-3.html", {"services": services, "projects": projects})

def contactView(request, *args, **kwargs):
    return render(request, "runok/contact.html", {})

def faqView(request, *args, **kwargs):
    return render(request, "runok/faq.html", {})

def aboutView(request, *args, **kwargs):
    return render(request, "runok/about.html", {})

def serviceView(request, url_title, *args, **kwargs):
    services = Service.objects.all()
    service = services.get(url_title=url_title)
    return render(request, "runok/service-details.html", {"services": services, "service": service})

def projectView(request, url_title, *args, **kwargs):
    project = Project.objects.get(url_title=url_title)
    return render(request, "runok/project-details.html", {"project": project})

def notFoundView(request, *args, **kwargs):
    return render(request, "runok/error.html", {})

def index1(request, *args, **kwargs):
    return render(request, "runok/index.html", {})

def index2(request, *args, **kwargs):
    return render(request, "runok/index-2.html", {})

def index3(request, *args, **kwargs):
    return render(request, "runok/index-3.html", {})

def index4(request, *args, **kwargs):
    return render(request, "runok/index-4.html", {})

def index5(request, *args, **kwargs):
    return render(request, "runok/index-5.html", {})

def index6(request, *args, **kwargs):
    return render(request, "runok/index-6.html", {})