from django.urls import path

from . import views

app_name = 'product_app'

urlpatterns = [
    path(
        'product_register/',
        views.RegisterView.as_view(),
        name='product_register'
    ),
    path(
        'product_list/',
        views.ProductsListView.as_view(),
        name='product_list'
    ),
    path(
        'search/',
        views.ProductSellView.as_view(),
        name='search'
    ),
    path(
        'buy_product/<pk>',
        views.BuyProductView.as_view(),
        name='buy_product'
    ),
    path(
        'update_product/<pk>',
        views.UpdateProductView.as_view(),
        name='update_product'
    ),
    path(
        'delete_product/<pk>',
        views.DeleteProductView.as_view(),
        name='delete_product'
    ),
]

