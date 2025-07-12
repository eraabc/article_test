from django import  forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='Title',
                            max_length=100,
                            required=True,
                            widget=forms.
                            TextInput(attrs={'class':'form-control'}),
                            error_messages={'required':'Please enter a title'})
    author = forms.CharField(label='Author', max_length=40,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Content',required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
