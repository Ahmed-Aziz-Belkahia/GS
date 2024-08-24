from django.contrib import admin
from .models import Service, Project, Member, Social, ContactInfo, FAQ, Client, ContactSubmission

# Register your models here.
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Social)
admin.site.register(ContactInfo)
admin.site.register(FAQ)
admin.site.register(Client)
admin.site.register(ContactSubmission)