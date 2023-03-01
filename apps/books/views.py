from django.shortcuts import render
from rest_framework import generics, status
from .models import Book, Authors
from .serializer import AuthorsSerializer, BookssSerializer
from rest_framework.response import Response


# Create your views here.
# books
class BookssCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookssSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate = Book.objects.filter(name=request.data['name'])
        if validate:
            return Response({'message': 'el nombre del libro ya existe'})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El libro fue creado correctamente'})



class BookssList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookssSerializer


class BookssDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookssSerializer


class BookssUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookssSerializer

    #def patch(self, request, pk=None):
    #    bookss=self.get_queryset().filter().first()
    #    if bookss:
    #        bookss_serializer = self.serializer_class(bookss)
    #        return Response(bookss_serializer.data, status=status.HTTP_200_OK)
    #    return Response({'error':'No existe libro con esoso datos'}, status=status.HTTP_400_BAD_REQUEST)


class BookssDestroy(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookssSerializer
    #lookup_field = 'pk'

    # def delete(self, request):
    #    books = self.get_queryset()
    #    if books > 0:
    #        books -= 1
    #        books.save()
    #        return Response({'copias': books})
    #    return super().delete(request)


# 7436



# author
class AuthorCreateView(generics.CreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate = Authors.objects.filter(name =request.data['name'])
        if validate:
            return Response({'message': 'el autor ya existe'})
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'el autor fur creado'})


class AuthorsList(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class AuthorsDetail(generics.RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class AuthorsUpdate(generics.UpdateAPIView):
    queryset = Authors.objects.all()
    serializer_class = BookssSerializer

     # def patch(self, request, pk=None):
     #     author = self.get_queryset().filter().first()
     #   if author:
     #       author_serializer = self.serializer_class(author)
     #       return Response(author_serializer.data, status=status.HTTP_200_OK)
     #   return Response({'error':'No existe libro con esoso datos'}, status=status.HTTP_400_BAD_REQUEST)


class AuthorsDestroy(generics.DestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

    # def delete(self, request):
    #    author = self.get_queryset()
    #    if author > 0:
    #        author -= 1
    #        author.save()
    #        return Response({'author': author})
    #    return super().delete(request)
