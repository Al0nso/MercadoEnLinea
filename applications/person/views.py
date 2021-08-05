from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import (
    View,
    UpdateView
)

from .forms import PersonForm, LoginForm
from .models import User
from .functions import pass_generator
from .mixins import BuyerMixin, SellerMixin

# Create your views here.
class RegisterView(FormView):
    template_name = 'person/register.html'
    form_class = PersonForm
    success_url = reverse_lazy('person_app:login')

    def form_valid(self, form):
        password = pass_generator()

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            password,
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            phone = form.cleaned_data['phone'], 
            user_type = form.cleaned_data['user_type'],
        )
        subject = 'Contraseña generada para el usuario: ' + str(form.cleaned_data['username'])
        message = 'La contraseña es: ' + password
        from_email = 'onlinemarket2021@gmail.com'
        send_mail(subject, message, from_email, [form.cleaned_data['email']])
        # return HttpResponseRedirect(
        #   reverse(
        #       'person_app:login'
        #   )
        # )
        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = 'person/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'person_app:login'
            )
        )

class AddMoneyView(BuyerMixin, UpdateView):
    template_name = 'person/add_money.html'
    model = User
    fields = [
        'money',
    ]
    success_url = reverse_lazy('product_app:search')

