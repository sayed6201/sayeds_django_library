===============================================================
views.py
===============================================================
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



===============================================================
index.html
===============================================================
{% extends 'book_outlet/base.html' %}

{% block title %}
All books
{% endblock  %}


{% block content %}

    <ul>
    {% for book in books %}
        <li>
        <a href="{{ book.get_absolute_url }}">
        {% comment %} <a href="{% url 'detail-page' book.id %}"> {% endcomment %}
            {{book.title}}, rating: {{book.rating}}
        </a>
        </li>
    {% endfor %}
    
    </ul>

    <hr>

    <p>Total number of Books: {{ num_book }}</p>
    <p>Average rating: {{ ratings_dic.rating__avg }}</p>
    <p>Rating info: {{ ratings_dic }}</p>

{% endblock  %}


===============================================================
detail-page.html
===============================================================
{% extends 'book_outlet/base.html' %}

{% block title %}
    {{title}}
{% endblock  %}


{% block content %}
    <h1>{{ title }}</h1>
    <h2>{{ author }}</h2>
    <p> The book has a rating of {{ rating }} </p>


    {% if is_bestselling %}
        <p>It is a bestseller</p>
    {% else %} 
        <p>It is not a bestseller</p>
    {% endif %}

{% endblock  %}


