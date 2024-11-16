from .models import Comment, Method, About
from django.utils.text import slugify
from django import forms
from django_summernote.widgets import SummernoteWidget


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
            'title', 'slug', 'purpose', 'summary', 'instructions', 'material',
            'prep_time', 'duration', 'alt_atr', 'group_size_min', 'group_size_max',
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

    # Automatically generate the slug based on the title if not provided. 
    def clean_slug(self): 
        title = self.cleaned_data.get('title')
        slug = self.cleaned_data.get('slug')
        
        # If slug is not provided, generate it from the title
        if not slug and title:
            slug = slugify(title)
            self.cleaned_data['slug'] = slug  # Ensure the generated slug is included in cleaned data

        
        return slug

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'body']