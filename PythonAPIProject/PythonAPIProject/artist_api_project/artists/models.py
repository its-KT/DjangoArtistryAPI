# artists/models.py
from django.contrib.auth.models import User
from django.db import models

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_TYPES)

    def __str__(self):
        return f"{self.get_work_type_display()} - {self.link}"

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
