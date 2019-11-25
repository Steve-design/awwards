from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['post_rated', 'score']    