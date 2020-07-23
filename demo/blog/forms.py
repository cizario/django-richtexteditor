from django import forms

from django_richtexteditor.widgets import RichTextarea

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'title *', 'autocomplete': 'off'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Content *', 'autocomplete': 'off'}),
            # 'excerpt': forms.Textarea(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Excerpt *', 'rows': 3, 'autocomplete': 'off'}),
            'content': RichTextarea(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Content *', 'autocomplete': 'off'}),
            'excerpt': RichTextarea(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Excerpt *', 'rows': 3, 'autocomplete': 'off'}),
        }
