from django.db.models import fields
from book.models import Api, Book 
from rest_framework import serializers 

class BookSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Book 
        fields = "__all__"

class ApiSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Api 
        fields =  "__all__"      