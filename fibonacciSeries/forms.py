from django import forms
class inputform(forms.Form):
    number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter number'}), required=True)
    
