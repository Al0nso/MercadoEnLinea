from django.urls import path

from . import views

app_name = 'person_app'

urlpatterns = [
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ), 
    path(
        'login/', 
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'add_money/<pk>',
        views.AddMoneyView.as_view(),
        name='add_money'
    ),
]

