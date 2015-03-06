from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "What does your mom call you?",
                                                                        "onblur": "if(this.value=='')this.value='What does your mom call you?'",
                                                                        "onfocus": "if(this.value=='What does your mom call you?')this.value=''",
                                                                        "value": "What does your mom call you?"}))
    message = forms.CharField(widget=forms.Textarea(attrs={
                                                            "placeholder": "What is on your mind?",
                                                            "onfocus": "if(this.value=='What is on your mind?')this.value=''",
                                                            "onblur": "if(this.value=='')this.value='What is on your mind?'"
                                                            }))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Where can I email you back?",
                                                             "onblur": "if(this.value=='')this.value='Where can I email you back?'",
                                                             "onfocus": "if(this.value=='Where can I email you back?')this.value=''",
                                                             "value": "Where can I email you back?"}))
    cc_myself = forms.BooleanField(required=False)