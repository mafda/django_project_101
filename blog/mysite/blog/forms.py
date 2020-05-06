from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author':forms.Select(attrs={'class':'postform form-control'}),
            'title':forms.TextInput(attrs={'class':'postform form-control textinputclass'}),
            'text':forms.Textarea(attrs={'class':'posttext editable medium-editor-textarea'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'postform form-control'}),
            'text':forms.Textarea(attrs={'class':'posttext editable medium-editor-textarea'})
        }