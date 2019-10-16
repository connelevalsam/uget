from django import forms

from .models import Order


class OrderForm(forms.Form):
    fullname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'br2 pa2'
            }
        )
    )

    email = forms.EmailField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                # 'placeholder': 'Enter your E-mail',
                'class': 'form-control'
            }
        )
    )
    address = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 7,
                'cols': 25
            }
        ),
        max_length=2000
    )
