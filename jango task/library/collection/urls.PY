from django.contrib import admin
from django.urls import path
from .import views
from .views import  book_delete_view ,book_list_create_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.library, name='library_books'),
    path('welcome', views.welcome, name='welcome'),
    path('favorites/', views.favorites, name='favorites'),
    path('books/', book_list_create_view , name='book-list'),
    path('books/<int:pk>/', book_delete_view , name='book-detail'),
    
   
]
    
    
    
