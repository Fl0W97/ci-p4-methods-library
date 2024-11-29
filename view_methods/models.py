from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"), (1, "Published")
)
LOCATION_CHOICES = (
    ('indoor', "Indoor"), ('outdoor', "Outdoor"),
    ('indoor/outdoor', "Indoor/Outdoor"),
)
PREPTIME_CHOICES = (
    ('up to 5mins', "up to 5mins"), ('up to 10mins', "up to 10mins"),
    ('up to 20mins', "up to 20mins"), ('more than 20mins', "more than 20mins")
)
choices = DURATION_CHOICES = (
    ('up to 10mins', "up to 10mins"), ('up to 20mins', "up to 20mins"),
    ('up to 30mins', "up to 30mins"), ('up to 60mins', "up to 60mins"),
    ('more than 60mins', "more than 60mins")
)
choices = PURPOSE_CHOICES = (
    ('idea generation', "Idea Generation"),
    ('team forming, development', "Team Forming, Development"),
    ('task structuring, prioritization', "Task Structuring, Prioritization"),
    ('conflict resolution', "Conflict Resolution"),
    ('continuous improvement, retrospectives',
     "Continuous Improvement, Retrospectives"),
    ('alignment of vision and goals', "Alignment of Vision and Goals"),
    ('facilitating effective planning', "Facilitating Effective Planning")
)

# Method model
class Method(models.Model):
    title = models.CharField(
        max_length=150, unique=True, blank=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="methods_library_methods"
    )
    slug = models.SlugField(
        max_length=150, unique=True, blank=False
    )
    purpose = models.CharField(
        max_length=255, choices=PURPOSE_CHOICES
    )
    summary = models.CharField(
        max_length=300,
        help_text="This text is shown on the landing page as short"
        " explanation of the methodology",
        default="No summary provided",
        blank=False
    )
    instructions = models.TextField(
        max_length=4000, blank=False
    )
    featured_image = CloudinaryField(
        'image', blank=True, null=True, default='placeholder',
        help_text="Recommended image size: 700x280px."
                  "Maximum file size: 3MB."
    )
    material = models.TextField(
        max_length=255, blank=False
    )
    prep_time = models.CharField(
        max_length=100,
        choices=PREPTIME_CHOICES, # Restrict Prep time
        help_text="Enter preparation time"
    )
    duration = models.CharField(
        max_length=100,
        choices=DURATION_CHOICES, # Restrict duraction
        help_text="Enter duration of the excercise"
    )
    alt_atr = models.CharField(
        max_length=150, blank=True, null=True
    )
    group_size_min = models.IntegerField(
        default=2  # Minimum group size
    )
    group_size_max = models.IntegerField(
        default=3  # Maximum group size
    )
    location = models.CharField(
        # Restrict location to indoor/outdoor/remote
        choices=LOCATION_CHOICES, default='indoor'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    status = models.IntegerField(
        # Restrict status to draft/published
        choices=STATUS, default=0
    )
    remote = models.BooleanField(
        default=False,
        help_text="Check if the method can be also"
                  " used for a remote session"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f" title {self.title} | written by {self.author}"

""" Comment model / Reused code from Code Institute
    see README.md credit section reused code """
class Comment(models.Model):
    method = models.ForeignKey(
        Method, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField(
        max_length=500
    )
    approved = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return (
            f" By {self.author} | {self.body} | Created on {self.created_on}"
        )

# model for like button
class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    method = models.ForeignKey(
        Method, on_delete=models.CASCADE, related_name='likes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        # Ensures that a user can like a method only once
        unique_together = ('user', 'method')

    def __str__(self):
        return f"{self.user.username} liked {self.method.title}"

    # Optionally, create a method to count likes for a method
    @classmethod
    def get_likes_for_method(cls, method):
        return cls.objects.filter(method=method).count()


""" model for about page / Reused code from Code Institute
    see README.md credit section reused code """
class About(models.Model):
    title = models.CharField(
        max_length=200, default="About Us"
    )
    body = models.TextField(
        help_text="Only the first about entry in the admin panel"
        " is displayed on the website.")

    def __str__(self):
        return self.title  # Show the title in the admin panel
