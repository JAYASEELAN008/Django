from django import views
from django.urls import path
from django.contrib import admin
from .views import home , product_details , category_products
from shoping import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
 path('admin/', admin.site.urls),
 path('',home , name = 'home'),
 path('product/<int:product_id>', product_details , name = "product_details" ),
 path('category/<int:category_id>', category_products , name = "category_products"),
 path('search/', views.search_products, name='search_products'),
 path('carsoule/', views.carsoule_products, name='carsolue_products'),
 path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
 path('cart/', views.view_cart, name='view_cart'),
 path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
 path('rate-product/<int:product_id>/', views.rate_product, name='rate_product'),
 path('offers/', views.offers, name='offers'),  
    



 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




