from django import forms
from Pages.models import Page, Category

class FormArticles(forms.Form):

    title = forms.CharField(label="Titulo")
    content = forms.CharField(label="Contenido", widget=forms.Textarea)




