from django.contrib.auth import authenticate
from django import forms

from .models import User

class PersonForm(forms.ModelForm):
    '''
    Forms for person requiring:
    - username
    - name
    - last_name
    - email
    - phone
    '''
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'last_name',
            'email',
            'phone',
            'user_type'
        ]

    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        try:
            user = User.objects.get(username=cleaned_data['username'])
        except:
            return self.cleaned_data
        raise forms.ValidationError('El nombre de usuario ya existe, elige otro')

class LoginForm(forms.Form):
    '''
    Forms for login requiring:
    - username
    - password
    '''
    username = forms.CharField(
        label = 'Nombre de Usuario',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Escribe tu nombre de usuario'
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Escribe tu contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        return self.cleaned_data
