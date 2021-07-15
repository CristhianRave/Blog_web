from django.shortcuts import render
from .models import Page, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


""" Recuperamos el slug (podria ser id en su lugar)
    introducido en la web para verificar que exista y obtener sus valores """
@login_required(login_url='/login')
def blog_p (request, slug):
    
    blog_p = Page.objects.get(slug=slug)    

    return render (request, 'posts/entrada_individual.html',{
        "blog" : blog_p,
    })


@login_required(login_url='/login')
def blog (request):

    articles = Page.objects.all()

# Montamos sistema de paginacion
    paginator = Paginator(articles, 6) # cantidad de articulos por pagina
    page = request.GET.get('page') # Recogemos el parametro 'page'
    page_articles = paginator.get_page(page) # Pasamos el numero de la pagina

    return render (request,'posts/entradas_blog.html',{
        "articles" : page_articles,
    }) 


@login_required(login_url='/login')
def category (request,category_id):

    category = Category.objects.get(id=category_id)
    articles = Page.objects.filter(categories=category)

    paginator = Paginator(articles, 6) # cantidad de articulos por pagina
    page = request.GET.get('page') # Recogemos el parametro 'page'
    page_articles = paginator.get_page(page) # Pasamos el numero de la pagina

    return render (request,'posts/category.html',{
        "category": category,
        "articles" : page_articles,
    }) 
