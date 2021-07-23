from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book, Api
from rest_framework import viewsets, permissions 
from .serializers import ApiSerializer, BookSerializer 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
import random 
import string 
# Create your views here.

from rest_framework_api_key.permissions import HasAPIKey

def book_list_ui(request):
    books = Book.objects.all()
    return render(request, "booklist.html", {"books": books })

def book_delete_ui(request, pk): 
    book = Book.objects.get(id=pk)
    book.delete() 
    return redirect("/book_list_ui/")


@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def book_add(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(["DELETE"])
def book_delete(request, pk): 
    book = Book.objects.get(id=pk)
    book.delete()
    return Response("Successfully deleted!")

@api_view(["PUT"])
def book_update(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def make_api_key(request): 


    return render(request, "make.html")

def generate(request): 
    if request.method == "POST": 
        user = request.POST["user"]
        mode = request.POST["nacin"]
        letters = string.ascii_letters 
        value = ''.join(random.choice(letters) for i in range(1,10))
        api = Api.objects.all()
        data =  [user, mode, value]
        serializer = ApiSerializer(api, data)
        if serializer.is_valid():
            serializer.save() 
        return render(request, "uspesno.html", {"value": value})

    return Response("Greska")


