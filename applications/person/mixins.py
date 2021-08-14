from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import User

def check_ocupation_user(ocupation, user_ocupation):
    if(ocupation == user_ocupation):
        return True
    else:
        return False

class BuyerMixin(LoginRequiredMixin):
    login_url = reverse_lazy('person_app:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not check_ocupation_user(request.user.user_type, User.BUYER):
            return HttpResponseRedirect(
                reverse(
                    'person_app:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)

class SellerMixin(LoginRequiredMixin):
    login_url = reverse_lazy('person_app:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not check_ocupation_user(request.user.user_type, User.SELLER):
            return HttpResponseRedirect(
                reverse(
                    'person_app:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)

