from django import forms

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

from blog.models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')
