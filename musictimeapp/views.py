from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView


from .forms import CustomUserCreationForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the musictime index.")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class login_view(LoginView):
    # The line below overrides the default template path of <appname>/<modelname>_login.html
    template_name = 'musictime/login.html'
     # Where accounts/login.html is the path under the templates folder as defined in your settings.py file
