from collections import UserDict

from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(
        label="Nome completo",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-sm",
            "placeholder": "Ex: Maria Silva",
            "autocomplete": "name"
        })
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "form-control shadow-sm",
            "placeholder": "seu@email.com",
            "autocomplete": "email"
        })
    )

    content = forms.CharField(
        label="Mensagem",
        max_length=500,
        widget=forms.Textarea(attrs={
            "class": "form-control shadow-sm",
            "placeholder": "Como podemos ajudar com sua compra?",
            "rows": 4
        })
    )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError ("O Email deve ser gmail.com!")
        return email


class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class resgisterForm(forms.Form):
    username= forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if not "gmail.com" in email:
            raise forms.ValidationError ("O Email deve ser gmail.com!")

        if qs.exists():
            raise forms.ValidationError("Esse email já existe")
        return email


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuário ja esxiste")
        return username


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("As senhas precisam ser iguais!")
        return data