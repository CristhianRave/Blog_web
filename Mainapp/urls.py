
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index' ),
    path('inicio/', views.index, name='Inicio' ),
    path('sobre-nosotros/', views.about_us, name='Sobre_nosotros' ),
    path('registro/', views.register_page , name='Registro' ),
    path('login/', views.login_page, name='Login' ),
    path('logout/', views.logout_user, name='Logout' ),
]