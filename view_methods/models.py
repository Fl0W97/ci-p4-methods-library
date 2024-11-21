from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
LOCATION_CHOICES = (('indoor', "Indoor"), ('outdoor', "Outdoor"), ('indoor/outdoor', "Indoor/Outdoor"))
PREPTIME_CHOICES = (('up to 5mins', "up to 5mins"), ('up to 10mins', "up to 10mins"), ('up to 20mins', "up to 20mins"), ('more than 20mins', "more than 20mins"))
choices=DURATION_CHOICES = (('up to 10mins', "up to 10mins"), ('up to 20mins', "up to 20mins"), ('up to 30mins', "up to 30mins"), 
('up to 60mins', "up to 60mins"), ('more than 60mins', "more than 60mins"))
choices=PURPOSE_CHOICES = (('idea generation', "Idea Generation"), ('team forming, development', "Team Forming, Development"), 
('task structuring, prioritization', "Task Structuring, Prioritization"), ('conflict resolution', "Conflict Resolution"), 
('continuous improvement, retrospectives', "Continuous Improvement, Retrospectives"), ('alignment of vision and goals', "Alignment of Vision and Goals"), 
('facilitating effective planning', "Facilitating Effective Planning"))

# Create your models here.
class Method(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="methods_library_methods"
    )
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    purpose = models.CharField(max_length=255, choices=PURPOSE_CHOICES)
    summary = models.CharField(
        max_length=255,
        help_text="This text is shown on the dashboard as short explanation of the methodology",
        default="No summary provided",
        blank=False
    )
    instructions = models.TextField(max_length=2000, blank=False)
    featured_image = CloudinaryField('image', blank=True, null=True, default='placeholder')
    material = models.TextField(max_length=255, blank=False)
    prep_time = models.CharField(max_length=100, choices=PREPTIME_CHOICES, help_text="Enter preparation time")
    duration = models.CharField(max_length=100, choices=DURATION_CHOICES, help_text="Enter duration of the excercise")
    alt_atr = models.CharField(max_length=255, blank=True, null=True)
    group_size_min = models.IntegerField(default=2)  # Minimum group size
    group_size_max = models.IntegerField(default=3)  # Maximum group size
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
    body = models.TextField(max_length=500)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f" written by {self.author} | {self.body} | Created on {self.created_on}"

#new input for like button
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'method')  # Ensures that a user can like a method only once

    def __str__(self):
        return f"{self.user.username} liked {self.method.title}"

    # Optionally, create a method to count likes for a method
    @classmethod
    def get_likes_for_method(cls, method):
        return cls.objects.filter(method=method).count()


from django.db import models

# Content for about page
class About(models.Model):
    title = models.CharField(max_length=200, default="About Us") # title for the "About" page
    body = models.TextField(help_text="Write the whole content of the About page. Only the first about entry in the admin panel list  is displayed on the website.")  # This will store the content for the "About" page

    def __str__(self):
        return self.title  # Show the title in the admin panel