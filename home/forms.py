from django import forms
from .models import CommunityPost

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your thoughts...'}),
        }