from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)
    url_title = models.SlugField()
    image = models.ImageField(upload_to="service")
    banner = models.ImageField(upload_to="service", blank=True)
    example_image = models.ImageField(upload_to="service", blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    url_title = models.SlugField(blank=True)
    image = models.ImageField(upload_to="project", blank=True)
    banner = models.ImageField(upload_to="project", blank=True)
    example_image = models.ImageField(upload_to="service", blank=True)
    mini_description = models.TextField(blank=True)
    description_title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    client = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100, blank=True)
    challange = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    result = models.TextField(blank=True)
    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to="member", blank=True, null=True)

class Social(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="socials")
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="client")
    role = models.CharField(max_length=100)
    testimonial = models.TextField()

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=50)
    message = models.TextField()