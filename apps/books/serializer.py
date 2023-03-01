from rest_framework import serializers
from .models import Book, Authors


class BookssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description')


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('name', 'nationality', 'book')
