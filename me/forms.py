from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'What\'s your mom call you?'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'What\'s on your mind?'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Where can we email you back?'}))
    cc_myself = forms.BooleanField(required=False)