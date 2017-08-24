from django import forms
from captcha.fields import ReCaptchaField
from .models import FeedBack, Comment


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)


class FeedbackForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'light',
    })

    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'message', 'captcha')


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'light',
    })

    class Meta:
        model = Comment
        fields = ('name', 'email', 'message', 'captcha')
