from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                          'id': 'form2Example17', 'type': 'text',
                                                          'placeholder': 'Телефон или электронная почта'}),
                            label="Телефон или электронная почта")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
                                                                 'id': 'form2Example17', 'type': 'password',
                                                                 'placeholder': 'Пароль'}),
                               label="Пароль")