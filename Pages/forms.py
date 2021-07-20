from django import forms
from Pages.models import Page, Category

class FormArticles(forms.Form):

    title = forms.CharField(label="Titulo", max_length=20)
    content = forms.CharField(label="Contenido", widget=forms.Textarea, required=False)
   




