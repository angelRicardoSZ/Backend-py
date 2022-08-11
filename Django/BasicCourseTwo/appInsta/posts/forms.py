"""Post forms"""

#Django

from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model form

    Args:
        forms (_type_): _description_
    """
    class Meta:
        
        model = Post
        
        fields = ('user', 'profile', 'title', 'photo')