from django.shortcuts import reverse
from django.views.generic import CreateView
from .form import RegisterForm


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('login')
