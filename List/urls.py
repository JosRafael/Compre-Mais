from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.lists, name='lists'),
    path('recipes/', views.recipes, name='recipes'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/', views.edit_product, name='edit_product'),

    path('add_list/', views.add_list, name='add_list'),
    path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),
    path('edit_list/', views.edit_list, name='edit_list'),
    path('edit_showlist/', views.edit_list, name='edit_list'),
    path('add_prod_in_list/<int:pk>/', views.add_prod_in_list, name='add_prod_in_list'),

    path('show_list/<int:pk>/', views.show_list, name='show_list'), 
    path('showRecipt/<int:pk>/', views.show_recipt, name='show_recipt'), 
    path('show_list/<int:pk>/', views.delete_product_lista, name='delete_product_lista'), 



    path('add_recipt/', views.add_recipt, name='add_recipt'),
    path('delete_recipt/<int:pk>/', views.delete_recipt, name='delete_recipt'),
    path('edit_recipt/', views.edit_recipt, name='edit_recipt'),
    path('add_prod_in_recipt/<int:pk>/', views.add_prod_in_recipt, name='add_prod_in_recipt'),

    path('login/', views.page_login, name='page_login'),
    path('cadastro/', views.page_cadastro, name='page_cadastro'),
    path('efetuar_cadastro/', views.efetuar_Cadastro, name='efetuar_cadastro'),
    path('efetuar_login/', views.efetuar_Login, name='efetuar_login'),
    path('page_home/', views.page_home, name='page_home'),
    path('logout/', views.efetuar_Logout, name='logout'),
]
