from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(label='TITLE',  max_length=250)
    content = forms.CharField(label='CONTENT', widget=forms.Textarea)