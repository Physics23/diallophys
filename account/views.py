from django.shortcuts import render, redirect

#from django.core.urlresolvers import revers_lazy
from django.urls import reverse, reverse_lazy
#from django.forms import CreateView
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'



# Create your views here.
