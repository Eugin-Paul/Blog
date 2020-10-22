from django import forms
from tinymce import TinyMCE
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email','password1','password2']

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured')

class CommentForm(forms.ModelForm):
    comment_post = forms.CharField(widget = forms.Textarea(attrs = {
      'placeholder': 'Type Comment',
      'id': 'text_form',
      'name' : 'comment_post',
    }))

    class Meta:
        model = Comment
        fields = ('comment_post',)