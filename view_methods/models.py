from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
LOCATION_CHOICES = (('indoor', "Indoor"), ('outdoor', "Outdoor"), ('indoor/outdoor', "Indoor/Outdoor"))

# Create your models here.
class Method(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="methods_library_methods"
    )
    purpose = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, help_text="This text is shown on the dashboard as short explanation of the methodology")
    instructions = models.TextField()
    material = models.TextField()
    alt_atr = models.CharField(max_length=255, null=True)
    prep_time = models.DurationField(null=True, help_text="Enter preparation time in minutes")
    duration = models.DurationField(null=True, help_text="Enter excercise duration in minutes")
    group_size_min = models.IntegerField(default=1)  # Minimum group size
    group_size_max = models.IntegerField(default=1)  # Maximum group size
    location = models.CharField(choices=LOCATION_CHOICES, default='indoor')  # Restrict location to indoor/outdoor
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0) # Restrict status to draft/published

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f" title {self.title} | written by {self.author}"




class Comment(models.Model):
    method = models.ForeignKey(
        Method, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f" written by {self.author} | Created on {self.created_on}"