from catalog.models import Author, Book, BookInstance, Genre
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of the main objects
    num_books = Book.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status == 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context=context)