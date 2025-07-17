from django import  forms
from django.core.exceptions import ValidationError

from webapp.models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(label='Title',
#                             max_length=100,
#                             required=True,
#                             widget=forms.
#                             TextInput(attrs={'class':'form-control'}),
#                             error_messages={'required':'Please enter a title'})
#     author = forms.CharField(label='Author', max_length=40,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
#     content = forms.CharField(label='Content',required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at','slug']

        error_messages = {
            'title': {
                'required': 'Обязательна к заполнению',
            }
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('Нельзя так')
        return title

    def clean(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        if title and content and title == content:
            raise ValidationError('заголовок и контент не должны быть равными')
        return self.cleaned_data