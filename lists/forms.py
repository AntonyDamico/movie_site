from django import forms

class MovieForm(forms.Form):
    title = forms.CharField()
    poster = forms.CharField()
    year = forms.IntegerField()