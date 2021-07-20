from django.shortcuts import render, redirect
from .models import Page, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Pages.forms import FormArticles
import random


""" Recuperamos el slug (podria ser id en su lugar)
    introducido en la web para verificar que exista y obtener sus valores """


@login_required(login_url='/login')
def blog_p(request, slug):

    blog_p = Page.objects.get(slug=slug)

    return render(request, 'posts/entrada_individual.html', {
        "blog": blog_p,
    })


@login_required(login_url='/login')
def blog(request):
    categories = Category.objects.all()
    articles = Page.objects.all()

# Montamos sistema de paginacion
    paginator = Paginator(articles, 6)  # cantidad de articulos por pagina
    page = request.GET.get('page')  # Recogemos el parametro 'page'
    page_articles = paginator.get_page(page)  # Pasamos el numero de la pagina

    return render(request, 'posts/entradas_blog.html', {
        "articles": page_articles,
    })


@login_required(login_url='/login')
def category(request, category_id):

    category = Category.objects.get(id=category_id)
    articles = Page.objects.filter(categories=category)

    paginator = Paginator(articles, 6)  # cantidad de articulos por pagina
    page = request.GET.get('page')  # Recogemos el parametro 'page'
    page_articles = paginator.get_page(page)  # Pasamos el numero de la pagina

    return render(request, 'posts/category.html', {
        "category": category,
        "articles": page_articles,
    })


@login_required(login_url='/login')
def crear_articulo(request):
    user_id = request.POST.get('user')
    image = request.FILES.get('imagen')
    num_aleatory = random.randint(1,1000)
    category = request.POST.get('category') 
    if category is None:
        cat = 3
    else:
        cat = category

    if request.method == "POST":
        formulario = FormArticles(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            user = user_id
            title = data_form['title']
            content = data_form['content']
            slug = f"{title}{num_aleatory}"
            if image != None:
                image = image
            else:
                image = 'articles/fondo_3.jpg'

            article = Page(
                user_id=user,
                title=title,
                content=content,
                image=image,
                public=True,
                slug=slug
            )
            article.save()
            article.categories.add(cat) # Asignamos categoria al articulo

            return redirect('/blog')
            
    else:
        formulario = FormArticles()

    return render(request, 'posts/create_article.html', {
        "form": formulario,
    })


def editar_article(request, slug):
    article = Page.objects.get(slug=slug)

    return render(request, 'posts/editar.html', {
        "article": article,
    })


def editado(request, slug):
   
    article = Page.objects.get(slug=slug)
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('imagen')
    cat = request.POST.get('category')

    if request.method == 'POST':
        article.title = title
        article.content = content
        if image != None:
            article.image = image

        article.save()
        article.categories.clear()
        article.categories.add(cat) # Asignamos categoria al articulo
    return redirect ('../blog/'+ article.slug)


def delete_article (request,id):

    article = Page.objects.get(pk=id)
    article.delete()
    return redirect ('/blog')