from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from List.models import Product, Category, List, List_product
from List.models import Recipt, TagRecipt, ProductRecipt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import models


def index(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    tagRecipts = TagRecipt.objects.all
    recipts = Recipt.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
        'tagRecipts': tagRecipts,
        'recipts': recipts,
    }
    return render(request, 'index.html', context)

def lists(request):
    lists = List.objects.all
    context = {
        'lists': lists,
    }
    return render(request, 'lists.html', context)


def recipes(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    tagRecipts = TagRecipt.objects.all
    recipts = Recipt.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
        'tagRecipts': tagRecipts,
        'recipts': recipts,
    }
    return render(request, 'recipes.html', context)

def add_product(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = Category.objects.get(id = request.POST['category'])
        data = Product(
            name = name,
            description = description,
            category = category
        )
        data.save()
    return HttpResponseRedirect('/')


def edit_product_in_list(request,pk,id):

    if request.method == 'POST':
        list = List.objects.get(id = pk)
        prod = Product.objects.get(id = id)
        quantity = request.POST['quantity']
        second_option = Product.objects.get(id = request.POST['idSecondOption'])
        importance = request.POST['importance']
        data = List_product(
            product = prod,
            list = list,
            quantity = quantity,
            product_second_option = second_option,
            importance = importance,
        )
        data.save()

        return HttpResponseRedirect('/showlist/'+str(pk)+'/'+str(id)+'/')
    
def delete_product_lista(request,pk):
    produto = List_product.objects.get(product__id = pk )
    produto.delete()
    return redirect(show_list)


def delete_product(request, pk):
    #if request.method == 'POST':
    prod = Product.objects.get(id = pk)
    prod.delete()
    return HttpResponseRedirect('/') 


def edit_product(request):
    if request.method == 'POST':
        prod = Product.objects.get(id = request.POST['id'])
        prod.name = request.POST['name']
        prod.description = request.POST['description']
        category = Category.objects.get(id = request.POST['category'])
        prod.category = category
        prod.save()
    return HttpResponseRedirect('/') 

def add_list(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        name = request.POST['name']
        data = List(
            name = name,
        )
        data.save()
    return HttpResponseRedirect('/lists/')

def delete_list(request, pk):
    #if request.method == 'POST':
    list = List.objects.get(id = pk)
    list.delete()
    return HttpResponseRedirect('/lists/') 


def edit_list(request):
    if request.method == 'POST':
        list = List.objects.get(id = request.POST['id'])
        list.name = request.POST['name']
        list.save()
    return HttpResponseRedirect('/lists/') 

def edit_showlist(request,id):
    if request.method == 'POST':
        lista = List_product.objects.get(id = request.POST['id'])
        lista.product = request.POST['name']
        lista.list = List.objects.get(id = request.POST['id'])
  
        lista.quantity = request.POST['quantity']
        lista.product_second_option  = Product.objects.get(id = request.POST['idSecondOption'])
        lista.importance = request.POST['importance']
        
       
        lista.save()
    return HttpResponseRedirect('/showlist/'+str(id)+'/') 

def add_prod_in_list(request,pk):
    if request.method == 'POST':
        list = List.objects.get(id = pk)
        prod = Product.objects.get(id = request.POST['idProd'])
        quantity = request.POST['quantity']
        second_option = Product.objects.get(id = request.POST['idSecondOption'])
        importance = request.POST['importance']
        data = List_product(
            product = prod,
            list = list,
            quantity = quantity,
            product_second_option = second_option,
            importance = importance,
        )
        data.save()
    return HttpResponseRedirect('/show_list/'+str(pk)+'/')

def show_list(request,pk):
    list_products = List_product.objects.filter(list__id=pk)
    list = List.objects.get(id=pk)
    products = Product.objects.all()
    context = {
        'list_products': list_products,
        'list':list,
        'products': products,
    }
    return render(request, 'showlist.html', context)

def add_recipt(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        description = request.POST['description']
        tagCategory = TagRecipt.objects.get(id = request.POST['category'])
        data = Recipt(
            name = name,
            description = description,
            tagCategory = tagCategory
        )
        data.save()
    return HttpResponseRedirect('/recipes/')

def delete_recipt(request, pk):
    #if request.method == 'POST':
    recipt = Recipt.objects.get(id = pk)
    recipt.delete()
    return HttpResponseRedirect('/recipes/') 

def edit_recipt(request):
    if request.method == 'POST':
        recipt = Recipt.objects.get(id = request.POST['id'])
        recipt.name = request.POST['name']
        recipt.description = request.POST['description']
        tagCategory = TagRecipt.objects.get(id = request.POST['category'])
        recipt.tagCategory = tagCategory
        recipt.save()
    return HttpResponseRedirect('/recipes/')


def add_prod_in_recipt(request, pk):
    if request.method == 'POST':
        recipt = Recipt.objects.get(id = pk)
        prod = Product.objects.get(id = request.POST['idProd'])
        quantity = request.POST['quantity']
        data = ProductRecipt(
            product = prod,
            recipt = recipt,
            quantity = quantity,
        )
        data.save()
    return HttpResponseRedirect('/showRecipt/'+str(pk)+'/')

def show_recipt(request,pk):
    reciptProducts = ProductRecipt.objects.filter(recipt__id=pk)
    recipe = Recipt.objects.get(id = pk)
    products = Product.objects.all()
    context = {
        'reciptProducts': reciptProducts,
        'recipe': recipe,
        'products': products,
    }
    return render(request, 'showRecipt.html', context)

def page_login(request):
    return render(request, "login.html")

def page_cadastro(request):
    return render(request, "cadastro.html")

def page_home(request):
    return render(request, "index.html")

def efetuar_Cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get("name")
        emailcad = request.POST.get("email")
        senha = request.POST.get("password")
        confirmSenha = request.POST.get("password_repeat")

        # Verificar se o usuário já existe
        if User.objects.filter(username=nome).exists():
            msg = {
                'msg': 'Usuário já cadastrado'
            }
            return render(request, "cadastro.html", msg)

        # Verificar se o email já está em uso
        if User.objects.filter(email=emailcad).exists():
            msg = {
                'msg': 'E-mail já cadastrado'
            }
            return render(request, "cadastro.html", msg)

        # Verificar se as senhas coincidem
        if senha != confirmSenha:
            msg = {
                'msg': 'Senhas não conferem'
            }
            return render(request, "cadastro.html", msg)

        # Criar o usuário
        user = User.objects.create_user(username=nome, email=emailcad, password=senha)
        user.save()

        msg = {
            'msg': 'Usuário cadastrado com sucesso'
        }

        return render(request, 'login.html', msg)

    return render(request, "cadastro.html")


def efetuar_Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(page_home)
        else:
            return render(request, "login.html", {"msg": "Usuário ou senha incorretos"})

    return render(request, "login.html")

def efetuar_Logout(request):
    logout(request)
    return redirect('page_login')