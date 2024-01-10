from typing import Any
from django import forms
from django.core import validators

def a(data):
    if data.lower()[0]=='a':
        raise forms.ValidationError('Not startswith a or A')
class Createschool(forms.Form):
    Sname=forms.CharField(validators=[a,validators.MaxLengthValidator(5)])
    Sprinciple=forms.CharField()
    Sbranch=forms.CharField()
    Email=forms.EmailField()
    Reenter=forms.EmailField()
    botprohibited=forms.CharField(required=False,widget=forms.HiddenInput)
    def clean_botprohibited(self):
        d=self.cleaned_data['botprohibited']
        if len(d)>0:
            raise forms.ValidationError('bot')
    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data['Reenter']
        if e!=r:
            raise forms.ValidationError('email are not same')