===============================================================
SAVE
===============================================================
>>> from book_outlet.models import Book

>>> harry_potter = Book(title="Hary poter1", rating = 5)
>>> harry_potter.save()

>>> lord_of_the_rings = Book(title="LOR", rating = 4)
>>> lord_of_the_rings.save()                         

>>> Book.objects.all()
	<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>

>>> Book.objects.create(title="Harry potter 2", rating=5,author="Sayed",is_bestselling=True) 
<Book: Harry potter 2 5>

>>> Book.objects.create(title="Random Book", rating=3,author="Ahmed",is_bestselling=False)   
<Book: Random Book 3>
>>> 


===============================================================
ACCESS
===============================================================
>>> from book_outlet.models import Book

>>> Book.objects.all()
	<QueryerySet [<Book: Hary poter1 5>, <Book: LOR 4>]>

>>> Book.objects.all()   
	<QuerySet [<Book: Hary poter1 5>, <Book: LOR 4>]>

>>> Book.objects.all()[1]
	<Book: LOR 4>

>>> Book.objects.all()[1].rating
	4

>>> Book.objects.all()[1].is_bestselling
	False


===============================================================
UPDATE
===============================================================
>>> harry_potter = Book.objects.all()[0]
>>> harry_potter.title
	'Hary poter1'

>>> lor = Book.objects.all()[1]
>>> lor.title
	'LOR'

>>> harry_potter.title = "JK Rowling"
>>> harry_potter.is_bestselling = True
>>> harry_potter.save()               
>>> Book.objects.all()[0]
	<Book: JK Rowling 5>


===============================================================
DELETE
===============================================================
>>> LOR = Book.objects.all()[1]
>>> LOR.delete()
	(1, {'book_outlet.Book': 1})

>>> Book.objects.all() 
	<QuerySet [<Book: JK Rowling 5>]>>>>


===============================================================
FILTER:
	https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
		• in Djang0, 
		• rating > 4 -> rating__gt = 4
		• rating <=5 -> rating__lte=5 
===============================================================


>>> Book.objects.get(id=3)
	<Book: Harry potter 2 5>

>>> Book.objects.get(title="Random Book")
	<Book: Random Book 3>

>>> Book.objects.get(is_bestselling=True) 
	ERR. Get can only return single result
	
>>> Book.objects.filter(is_bestselling=True) 
	<QuerySet [<Book: JK Rowling 5>, <Book: Harry potter 2 5>]>

>>> Book.objects.filter(is_bestselling=False, rating=3) 
	<QuerySet [<Book: Random Book 3>]>

>>> Book.objects.filter(rating>3)                       
	Err Not Suported

>>> Book.objects.filter(rating__gt=3) 
	<QuerySet [<Book: JK Rowling 5>, <Book: Harry potter 2 5>]>

>>> Book.objects.filter(rating__lt=3) 
	<QuerySet []>

>>> Book.objects.filter(rating__gte=3, title__contains="story")
	<QuerySet []>

>>> Book.objects.filter(rating__gte=3, title__contains="Book")  
	<QuerySet [<Book: Random Book 3>]>

>>> Book.objects.filter(rating__gte=3, title__contains="book") 
	<QuerySet [<Book: Random Book 3>]>


===============================================================
FILTER:
	FILTER with and , or:
===============================================================

>>> from django.db.models import Q

>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True)) 
	<QuerySet [<Book: JK Rowling 5>, <Book: Harry potter 2 5>]>

>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(title="Harry potter 2")) 
	<QuerySet [<Book: Harry potter 2 5>]>

>>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), title="Harry potter 2")    
	<QuerySet [<Book: Harry potter 2 5>]>
	

===============================================================
Nested Query:
===============================================================
>>> from book_outlet.models import Book

>>> Book.objects.all()
	<QuerySet [<Book: JK Rowling 5>, <Book: Harry potter 2 5>, <Book: Random Book 3>]>

>>> Book.objects.get(title="Harry potter 2").save()  
>>> Book.objects.get(title="Harry potter 2").slug  
	'harry-potter-2'


===============================================================
Aggregation function:
===============================================================

from django.db.models import Avg, Max, Min

   books = Book.objects.all().order_by("-rating") # - -> orders descending order

   num_booka = books.count

   ratings_dic = books.aggregate(Avg("rating"), Min("rating")) # returns dcitionary with keys: rating__avg, rating__min

	

