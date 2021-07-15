from django.contrib import admin
from .models import Page, Category


# Configuracion extras

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('name', )
    list_display = ('name','description','created_at')
    ordering = ('created_at',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')
    list_filter = ('public','user','categories')
    list_display = ('title','user','created_at','public')
    ordering = ('created_at',)

    """ Usamos esta funcion para obtener el user cuando aplicamos el Editable=False en models """
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


# Register your models here.

admin.site.register(Page, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)


#Configuracion del panel de admin
title = 'Blog Web'
subtitle = 'Panel de gestion'

admin.site.site_header = title  
admin.site.site_title = title  
admin.site.index_title = subtitle  

