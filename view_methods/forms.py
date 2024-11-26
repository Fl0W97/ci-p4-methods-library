from .models import Comment, Method, About
from django.utils.text import slugify
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError
from urllib.parse import urlparse


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

        # If the image is uploaded as a URL (Cloudinary might return a URL as a string)
        if isinstance(featured_image, str):  # Cloudinary returns URLs as strings
            # It's already a valid image URL, so we just return it as is
            return featured_image

        # # If it's a file object (meaning the user uploaded a file)
        if hasattr(featured_image, 'size'):
            max_size = 3 * 1024 * 1024  # 3MB limit
            if featured_image.size > max_size:
                raise ValidationError("The image size must be less than 3MB.")
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


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'body']

"""
class MethodForm_custom(forms.ModelForm_custom):
    instructions = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Method
        fields = (
            'title', 'purpose', 'summary', 'instructions', 'material',
            'prep_time', 'duration', 'featured_image',
            'group_size_min', 'group_size_max', 'location', 'remote',
        )

    # Customizing the 'title' field (using TextInput)
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Bootstrap class
            'placeholder': 'Enter Method Title',
            'id': 'id_title',  # Custom ID
        })
    )

        # Customizing the 'purpose' field (using Select for choices)
    purpose = forms.ChoiceField(
        choices=Method.PURPOSE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_purpose',
        })
    )

        # Customizing the 'summary' field (using Textarea)
    summary = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a brief summary',
            'id': 'id_summary',
        })
    )

    # Customizing the 'instructions' field (using Textarea, potentially with Summernote integration)
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control summernote-editor',  # Add the Summernote class for rich text editing
            'id': 'id_instructions',
            'placeholder': 'Enter detailed instructions',
        })
    )

    # Customizing the 'material' field
    material = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_material',
            'placeholder': 'Enter required materials',
        })
    )

    # Customizing the 'prep_time' field (using Select for choices)
    prep_time = forms.ChoiceField(
        choices=Method.PREPTIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_prep_time',
        })
    )

    # Customizing the 'duration' field (using Select for choices)
    duration = forms.ChoiceField(
        choices=Method.DURATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_duration',
        })
    )

    # Customizing the 'group_size_min' field
    group_size_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_group_size_min',
            'placeholder': 'Enter minimum group size',
        })
    )

    # Customizing the 'group_size_max' field
    group_size_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_group_size_max',
            'placeholder': 'Enter maximum group size',
        })
    )

    # Customizing the 'location' field
    location = forms.ChoiceField(
        choices=Method.LOCATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_location',
        })
    )

        # Customizing the 'remote' field (using a Checkbox)
    remote = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'id_remote',
        })
    )

    # Customizing the 'featured_image' field
    featured_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
            'id': 'id_featured_image',
        })
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

        # If the image is uploaded as a URL (Cloudinary might return a URL as a string)
        if isinstance(featured_image, str):  # Cloudinary returns URLs as strings
            # It's already a valid image URL, so we just return it as is
            return featured_image

        # # If it's a file object (meaning the user uploaded a file)
        if hasattr(featured_image, 'size'):
            max_size = 3 * 1024 * 1024  # 3MB limit
            if featured_image.size > max_size:
                raise ValidationError("The image size must be less than 3MB.")
        else:
            raise ValidationError("The uploaded file is not a valid image.")

            return featured_image
"""