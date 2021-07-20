
from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog, name='Blog'),
    path('blog/<str:slug>', views.blog_p, name='Blog_p'),
    path('categoria/<int:category_id>', views.category, name='Category'),
    path('crear-articulo/', views.crear_articulo, name='Crear-articulo'),
    path('editar-articulo/<str:slug>', views.editar_article, name='Editar-articulo'),
    path('editar/<str:slug>', views.editado, name='Editar' ),
    path('eliminar-articulo/<int:id>', views.delete_article, name='Eliminar-articulo' ),
]
