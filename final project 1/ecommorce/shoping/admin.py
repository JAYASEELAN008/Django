from django.contrib import admin
from .models import Product , Category
# Register your models here.


admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'ratings', 'star_color']
    list_editable = ['star_color']

admin.site.register(Product, ProductAdmin)

