#============================================================================================================
#Relation Explanation
    #1) Book (M-1) Author -> One author can write many books
            # author = models.ForeignKey(Authors, on_delete= models.CASCADE, null= True, related_name= "books")

    #2) Address (1-1) Author -> Author has one address and vise-versa
            # address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="author", null=True)

    #3) Country (M-M) Book -> Book can be published in many countries, and one country can have multuple published book
            # published_countries = models.ManyToManyField(Country)

     NOTE: See related_models.py for detail. 

     https://docs.djangoproject.com/en/3.2/topics/db/examples/
#============================================================================================================	


===============================================================
( 1-1 and 1-M ) Related Data Save and Access (Book - > Author):
===============================================================
>> from book_outlet.models import Book, Authors
>>> jk = Authors(first_name="J.K", last_name="Rowling")
>>> jk.save()                                          
>>> Authors.objects.all()
	<QuerySet [<Authors: Authors object (1)>]>
	
>>> hp = Book(title="Harry potter 1", rating= 5, is_bestselling=True, slug="Haryy-potter-1", author=jk)
>>> hp.save()
>>> Book.objects.all()   
	<QuerySet [<Book: Harry potter 1 5>]>
	
>>> harrypotter = Book.objects.all()[0]
>>> harrypotter                        
	<Book: Harry potter 1 5>
>>> harrypotter.author
	<Authors: Authors object (1)>
>>> harrypotter.author.first_name
	'J.K'
>>> harrypotter.author.last_name 
	'Rowlin'


===============================================================
( 1-1 and 1-M ) Related Data Filter (Author -> Book):
===============================================================
>>> books_by_rowling = Book.objects.filter(author__last_name="Rowling")

>>> books_by_rowling = Book.objects.filter(author__last_name__contains="Rowl")

>>> books_by_rowling
	<QuerySet [<Book: Harry potter 1 5>]>


===============================================================
( 1-1 and 1-M ) Related Data Inverse Access (Author -> Book):
===============================================================
>>> jkr = Authors.objects.get(first_name="J.K")
>>> jkr
	<Authors: Authors object (1)>

#by default Book -> book
#You can change the name in models.py
#author = models.ForeignKey(Authors, on_delete= models.CASCADE, null= True, related_name= "books")

>>> jkr.book_set
	<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00000247F1C519A0>
>>> jkr.book_set.all()
	<QuerySet [<Book: Harry potter 1 5>]>
	>>>

#after setting ->  related_name= "books"
>> from book_outlet.models import Book, Authors        
>>> jkr = Authors.objects.get(first_name="J.K") 
>>> jkr.books.all()                            
	<QuerySet [<Book: Harry potter 1 5>]>
>>> jkr.books.get(title="Harry potter 1")
	<Book: Harry potter 1 5>
>>> jkr.books.filter(rating__gt=3)                
<QuerySet [<Book: Harry potter 1 5>]>



===============================================================
( M- M ) SAVE Many-Many Relation Query (Book -> Country) :
===============================================================
>>> from book_outlet.models import Country, Book

>>> germany = Country(name="Germany", code="DE")
>>> germany.save()

>>> hpl = Book.objects.all()[0]
>>> hpl.published_countries
	LIST
	<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000158069F97F0>
	
>>> hpl.published_countries.all()
	<QuerySet []>
	                          
>>> hpl.published_countries.add(germany)

===============================================================
( M- M ) Accessing Many-Many Related DB (Book -> Country): 
===============================================================
>>> hpl.published_countries             
	<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000015806A12FD0>
>>> hpl.published_countries.all()
	<QuerySet [<Country: Germany, DE>]>

===============================================================
( M- M ) Filtering Many-Many Related DB (Book -> Country) :
===============================================================
>>> hpl.published_countries.filter(code="UK")
	<QuerySet []>
	
>>> hpl.published_countries.filter(code="DE") 
	<QuerySet [<Country: Germany, DE>]>

Inverse Many-Many relation (Book -> Country) :
>>> Country.objects.all()                    
	<QuerySet [<Country: Germany, DE>]>
	
>>> Country.objects.all()[0]
	<Country: Germany, DE>
	
>>> Country.objects.all()[0].book_set.all()
<QuerySet [<Book: Harry potter 1 5>]>