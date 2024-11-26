from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer




def library(request):
    myhome= Book.objects.all().values()
    template = loader.get_template('library_books.html')
    context = {
        'myhome' : myhome,
    }
    return HttpResponse(template.render(context, request))


def welcome(request):
    context = {
        'greeting': "Welcome To The Site....!",
        'user_name': "FAISU", 
    }
    return render(request, 'welcome.html', context)


def favorites(request):
    context = {
        'favorite_items': ['python','django','APIs','web development']
    }
    return render(request, 'favorites.html', context)










@api_view(['GET', 'POST'])
def book_list_create_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)