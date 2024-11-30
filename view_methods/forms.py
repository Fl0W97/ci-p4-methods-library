from .models import Comment, Method, About
from django.utils.text import slugify
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError
from urllib.parse import urlparse
import os

""" class AboutForm / Reused code from Code Institute
    see README.md credit section reused code """


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class MethodForm(forms.ModelForm):
    instructions = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Method
        fields = (
            'title', 'purpose', 'summary', 'instructions', 'material',
            'prep_time', 'duration', 'featured_image',
            'group_size_min', 'group_size_max', 'location', 'remote',
        )

    # validation for group size
    def clean(self):
        cleaned_data = super().clean()
        group_size_min = cleaned_data.get('group_size_min')
        group_size_max = cleaned_data.get('group_size_max')

        if group_size_min > group_size_max:
            raise forms.ValidationError("Minimum group size cannot be greater"
                                        "than the maximum group size.")

        return cleaned_data

    # Add custom validation for image size
    def clean_featured_image(self):

        featured_image = self.cleaned_data.get('featured_image')

        # If the delete checkbox is checked, remove the image
        if self.cleaned_data.get('delete_featured_image'):
            # Remove the image by setting it to None (null in the database)
            return None

        # If no image is uploaded, just return None (allow empty value)
        if not featured_image:
            return None

        # If the image is uploaded as a URL (Cloud. return a URL as a string)
        if isinstance(featured_image, str):
            # It's already a valid image URL, so we just return it as is
            return featured_image

        # # If it's a file object (meaning the user uploaded a file)
        if hasattr(featured_image, 'size'):
            max_size = 3 * 1024 * 1024  # 3MB limit
            if featured_image.size > max_size:
                raise ValidationError("The image size must be less than 3MB.")

            # Check the file extension
            valid_extensions = ['.jpg', '.jpeg', '.png']
            # get the file extension
            file_extension = os.path.splitext(featured_image.name)[1].lower()

            if file_extension not in valid_extensions:
                raise ValidationError("Invalid file format. Only .jpg,"
                                      " .jpeg, .png are allowed.")

        else:
            raise ValidationError("The uploaded file is not a valid image.")

        return featured_image

    # Automatically generate the slug based on the title if not provided.
    def save(self, commit=True):

        instance = super().save(commit=False)

        # If slug is empty, generate one from the title
        if not instance.slug:
            # Slugify the title to create a unique slug
            instance.slug = slugify(instance.title)

        if commit:
            instance.save()
        return instance


""" form for about page / Reused code from Code Institute
    see README.md credit section reused code """


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'body']
