from django.contrib import admin
from .models import *
from main.views import ProductoImage

class ClienteInline(admin.TabularInline):
    model=Cliente

class ColaboradorInline(admin.TabularInline):
    model=Colaborador

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]

class ProductoImageInline(admin.TabularInline):
    model=ProductoImage

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ProductoImageInline,
    ]

admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)

admin.site.register(Localizacion)
#admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)