
from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog , name='Blog' ),
    path('blog/<str:slug>', views.blog_p , name='Blog_p' ),
    path('categoria/<int:category_id>', views.category, name='Category' ),

]