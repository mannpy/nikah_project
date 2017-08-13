from django import forms
from captcha.fields import ReCaptchaField
from .models import FeedBack


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)


class FeedbackForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'clean',
    })

    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'message', 'captcha')
