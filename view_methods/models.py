from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Method(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="methods_library_methods"
    )
    purpose = models.CharField(max_length=255)
    instructions = models.TextField()
    material = models.TextField()
    alt_atr = models.CharField(max_length=255)
    prep_time = models.TimeField()
    duration = models.DurationField()
    group_size = models.IntegerField()
    location = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} | written by {self.author}"