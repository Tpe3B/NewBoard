from django import forms

from mmorpg.models import Post, Answer


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


class AnswerForm(forms.ModelForm): #answer=reply
    class Meta:
        model = Answer#answer=reply
        fields = ['content']


class SendForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SendForm, self).__init__(*args, **kwargs)

    content = forms.CharField(required=True, max_length=400, label='Текст')
