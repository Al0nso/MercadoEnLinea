from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import (
    View,
    ListView,
    UpdateView,
    DeleteView,
)

from applications.person.models import User
from applications.person.mixins import SellerMixin, BuyerMixin
from .models import Product
from .forms import ProductForm

# Create your views here.
class RegisterView(SellerMixin, FormView):
    template_name = 'product/register.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_list')

    def form_valid(self, form):
        Product.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            price=form.cleaned_data['price'],
            photo=form.cleaned_data['photo'],
            owner=self.request.user
        )
        return super(RegisterView, self).form_valid(form)

class ProductsListView(LoginRequiredMixin, ListView):
    template_name = 'product/seller_list.html'
    context_object_name = 'seller_list'
    paginate_by = 5
    login_url = reverse_lazy('person_app:login')

    def get_queryset(self):
        list_products = Product.objects.filter(
            owner=self.request.user
        ).order_by('id')
        return list_products

class ProductSellView(BuyerMixin, ListView):
    template_name = 'product/products_list.html'
    context_object_name = 'list_products'
    paginate_by = 5

    def get_queryset(self):
        list_products = Product.objects.filter(
            is_sold=False
        ).order_by('id')
        return list_products

class BuyProductView(BuyerMixin, View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id = self.kwargs['pk'])
        product.owner.money += product.price
        product.owner.save()
        self.request.user.money -= product.price
        self.request.user.save()
        product.owner = self.request.user
        product.is_sold = True
        product.save()
        subject = 'Felicidades!! Compraste un producto'
        message = 'Haz realizado la compra del producto: ' + str(product.name) + ' Felicidades!!'
        from_email = 'onlinemarket2021@gmail.com'
        send_mail(subject, message, from_email, [self.request.user.email])

        return HttpResponseRedirect(
            reverse(
                'product_app:search'
            )
        )

class UpdateProductView(SellerMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_list')

class DeleteProductView(SellerMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('product_app:product_list')
