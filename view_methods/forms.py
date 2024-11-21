from .models import Comment, Method, About
from django.utils.text import slugify
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class MethodForm(forms.ModelForm):
    instructions = forms.CharField(widget=SummernoteWidget())
    summary = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model = Method
        fields = (
            'title', 'purpose', 'summary', 'instructions', 'material',
            'prep_time', 'duration', 'featured_image', 'alt_atr', 'group_size_min', 'group_size_max',
            'location',
        )

    # validation for group size
    def clean(self):
        cleaned_data = super().clean()
        group_size_min = cleaned_data.get('group_size_min')
        group_size_max = cleaned_data.get('group_size_max')

        if group_size_min > group_size_max:
            raise forms.ValidationError("Minimum group size cannot be greater than the maximum group size.")

        return cleaned_data


    # Add custom validation for image size in the same way as the group size validation
    def clean_featured_image(self):
        featured_image = self.cleaned_data.get('featured_image')

        # If the delete checkbox is checked, remove the image
        if self.cleaned_data.get('delete_featured_image'):
            # Remove the image by setting it to None (which will set it to null in the database)
            return None

        # If no image is uploaded, simply return the field value (which is None or empty)
        if not featured_image:
            return None

    # If an image is uploaded, validate it
        if hasattr(featured_image, 'size'):  # Check if it's a valid file object
            max_size = 2 * 1024 * 1024  # 2MB limit
            if featured_image.size > max_size:
                raise ValidationError("The image size must be less than 2MB.")
        else:
            raise ValidationError("The uploaded file is not a valid image.")
            
            return featured_image


    # Automatically generate the slug based on the title if not provided.
    def save(self, commit=True):
        instance = super().save(commit=False)
        # If slug is empty, generate one from the title
        if not instance.slug:
            instance.slug = slugify(instance.title)  # Slugify the title to create a unique slug
        if commit:
            instance.save()
        return instance

"""
    # Automatically generate the slug based on the title if not provided. 
    def clean_slug(self): 
        title = self.cleaned_data.get('title')
        slug = self.cleaned_data.get('slug')
        
        # If slug is not provided, generate it from the title
        if not slug and title:
            slug = slugify(title)
            self.cleaned_data['slug'] = slug  # Ensure the generated slug is included in cleaned data

        return slug


    # Add custom validation for image size
    def clean_featured_image(self):
        # Get the image file from cleaned data
        featured_image = self.cleaned_data.get('featured_image')

        if featured_image:
            # Ensure the uploaded file is not a string (which could happen if the field is empty)
            if isinstance(featured_image, str):  # This may happen if no image is provided
                return featured_image  # Return the image URL or string as is

            # Check image size (3MB size limit)
            max_size = 2 * 1024 * 1024  # 2MB size limit
            if featured_image.size > max_size:
                raise ValidationError('The file size must be less than 2MB.')

        return featured_image


    # Save the form, ensuring the slug is set properly
    def save(self, commit=True):
        method = super().save(commit=False)

        # If the slug is empty (i.e., it wasn't provided by the user), generate it from the title
        if not method.slug and method.title:
            method.slug = slugify(method.title)

        # Ensure that the status is always set to 'Draft' when a new method is created
        if commit:
            method.status = 0  
            method.save()

        return method
"""

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'body']