from django import forms
from website.models import Contact, Newsletter
# from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(max_length=100, initial='ناشناس', widget=forms.HiddenInput())
    email = forms.EmailField(max_length=225)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    

class ContactForm(forms.ModelForm):
        # captcha = CaptchaField()

        class Meta:
            model = Contact
            fields = '__all__'
            

    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        

