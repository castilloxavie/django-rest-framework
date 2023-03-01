from django.urls import path
from .views import BookssCreateView, BookssList, BookssDetail, BookssUpdate, BookssDestroy, AuthorCreateView, AuthorsList, AuthorsDetail, AuthorsUpdate, AuthorsDestroy

urlpatterns = [
    #books
    path('books_create/', BookssCreateView.as_view(), name='books_create'),
    path('books_list/', BookssList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookssDetail.as_view(), name='book_detail'),
    path('books_update/<int:pk>/', BookssUpdate.as_view(), name='books_update'),
    path('books_destroy/<int:pk>/', BookssDestroy.as_view(), name='books_destroy'),

    #authors
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors_list/', AuthorsList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorsDetail.as_view(), name='author_detail'),
    path('authors_update/', AuthorsUpdate.as_view(), name='authors_update'),
    path('authors_destroy/', AuthorsDestroy.as_view(), name='authors_destroy'),

]
