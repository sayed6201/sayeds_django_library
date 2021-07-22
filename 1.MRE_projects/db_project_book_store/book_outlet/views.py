from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating") # - -> orders descending order
    num_booka = books.count
    ratings_dic = books.aggregate(Avg("rating"), Min("rating")) # returns dcitionary with keys: rating__avg, rating__min

    return render(request,"book_outlet/index.html",
    {
        "books" : books,
        "num_book" : num_booka,
        "ratings_dic" : ratings_dic
    })


def book_detail(request, slug):

    # try:
    #     book = Book.objects.get(pk= id)
    #     # book = Book.objects.get(id= id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug = slug)
    return render(request, "book_outlet/book_detail.html",
    {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    }
    )