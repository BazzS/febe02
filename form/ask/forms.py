from django import forms

class InputForm(forms.Form):
    name0 = forms.CharField(label='name0',max_length=50)
