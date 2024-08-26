from django.shortcuts import render

from Pages.models import FAQ, Client, ContactInfo, ContactSubmission, Member, Service, Project

# Create your views here.

def index0(request, *args, **kwargs):
    faqs = FAQ.objects.all()
    info = ContactInfo.objects.first()
    clients = Client.objects.all()[:3]
    members = Member.objects.all()
    if request.method == 'POST':
        ContactSubmission.objects.create(first_name=request.POST.get("fullname"), last_name=request.POST.get("lastname"), email=request.POST.get("email"), phone=request.POST.get("phone"), message=request.POST.get("message"))
    services = Service.objects.all()
    projects = Project.objects.all()
    return render(request, "runok/index-3.html", {"services": services, "clients": clients, "projects": projects, "info": info, "faqs": faqs, "members": members})

def contactView(request, *args, **kwargs):
    info = ContactInfo.objects.first()
    if request.method == 'POST':
        ContactSubmission.objects.create(first_name=request.POST.get("fullname"), last_name=request.POST.get("lastname"), email=request.POST.get("email"), phone=request.POST.get("phone"), message=request.POST.get("message"))
    return render(request, "runok/contact.html", {"info": info})

def faqView(request, *args, **kwargs):
    return render(request, "runok/faq.html", {})

def aboutView(request, *args, **kwargs):
    clients = Client.objects.all()[:3]
    members = Member.objects.all()
    info = ContactInfo.objects.first()
    return render(request, "runok/about.html", {"info": info, "clients": clients, "members": members})

def serviceView(request, url_title, *args, **kwargs):
    info = ContactInfo.objects.first()
    services = Service.objects.all()
    service = services.get(url_title=url_title)
    return render(request, "runok/service-details.html", {"services": services, "service": service, "info": info})

def projectView(request, url_title, *args, **kwargs):
    info = ContactInfo.objects.first()
    project = Project.objects.get(url_title=url_title)
    return render(request, "runok/project-details.html", {"project": project, "info": info})

def notFoundView(request, *args, **kwargs):
    info = ContactInfo.objects.first()

    return render(request, "runok/error.html", {"info": info})

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