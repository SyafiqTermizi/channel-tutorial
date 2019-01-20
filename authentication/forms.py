from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    """
    Log user in using email address
    """

    email = forms.EmailField(required=True, label='',
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Email address',
                                 }
                             )
                          )
    password = forms.CharField(label='', strip=False,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Password',
                                   }
                               )
                            )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=self.cleaned_data.get('email'))
        except User.DoesNotExist:
            raise forms.ValidationError('Email address does not exist')

        if user and password:
            self.user_cache = authenticate(request=self.request, username=user,
                                           password=password)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                message='Account inactive',
                code='inactive'
            )

    def get_user(self):
        return self.user_cache
