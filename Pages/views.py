from django.shortcuts import render, redirect
from .models import Page, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Pages.forms import FormArticles
from django.contrib.auth.models import Group


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
    # category = request.POST.get('categoria') pendiente arreglar

    if request.method == "POST":
        formulario = FormArticles(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            user = user_id
            title = data_form['title']
            content = data_form['content']
            slug = f"{title}{user}"

            article = Page(
                user_id=user,
                title=title,
                content=content,
                public=True,
                slug=slug
            )

            article.save()

            return redirect('/blog')

    else:
        formulario = FormArticles()

    return render(request, 'posts/create_article.html', {
        "form": formulario,
    })
