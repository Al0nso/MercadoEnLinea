from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('person_app:login')
