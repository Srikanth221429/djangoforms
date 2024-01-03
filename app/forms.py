from django import forms


class Createschool(forms.Form):
    Sname=forms.CharField()
    Sprinciple=forms.CharField()
    Sbranch=forms.CharField()