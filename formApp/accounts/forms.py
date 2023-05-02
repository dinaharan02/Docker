from django import forms


class SignUpForm(forms.Form):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    mobile_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
