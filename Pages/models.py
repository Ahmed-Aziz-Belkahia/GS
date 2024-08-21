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