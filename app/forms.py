from django import forms

class MarvelForm(forms.Form):
    mname = forms.CharField(max_length=10)
    mid = forms.IntegerField()
    mlan = forms.CharField(max_length=10)
