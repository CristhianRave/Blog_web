from Pages.models import Page, Category


# Debemos registrar este context procesor en settings


def get_categories(request):

    categories_use = Page.objects.filter(
        public=True).values_list('categories', flat=True)

# Filtramos las categorias que tienen articulos relacionados
    categories = Category.objects.filter(id__in=categories_use).values_list(
        'id', 'name')

    return {
        'categories': categories,
        'ids': categories_use,
    }
