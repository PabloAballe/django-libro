from django import forms


class SheachForm(forms.Form):
    shearch = forms.CharField( label="", max_length=100 , widget= forms.TextInput
                           (attrs={'class':'form-control mr-sm-2'}))
