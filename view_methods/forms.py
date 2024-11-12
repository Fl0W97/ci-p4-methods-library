from .models import Comment
from .models import Method
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = (
            'title', 'slug', 'purpose', 'summary', 'instructions', 'material',
            'prep_time', 'duration', 'alt_atr', 'group_size_min', 'group_size_max',
            'location',
        )


    # validation
    def clean(self):
        cleaned_data = super().clean()
        group_size_min = cleaned_data.get('group_size_min')
        group_size_max = cleaned_data.get('group_size_max')

        if group_size_min > group_size_max:
            raise forms.ValidationError("Minimum group size cannot be greater than the maximum group size.")

        return cleaned_data


    def save(self, commit=True):
        method = super().save(commit=False)
        if commit:
            method.status = 0  # Ensure that the status is always set to 'Draft' when a new method is created
            method.save()
        return method