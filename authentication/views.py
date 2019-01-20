from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutnView
)
from django.shortcuts import reverse

from .forms import LoginForm


class LoginView(BaseLoginView):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('chats:index')


class LogoutView(BaseLogoutnView):

    def get_next_page(self):
        return reverse('authentication:login')


login_view = LoginView.as_view()
logout_view = LogoutView.as_view()
