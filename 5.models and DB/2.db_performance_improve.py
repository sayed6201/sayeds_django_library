===============================================================
Improving Performance:
===============================================================

	• Book(title="") -> Does not instantly hit the database. Have to call save()

	• bestseller = Book.objects.filter(is_bestselling=True) -> only storing the instance. 
															The DB is not hit yet. So good for performance

	• amaizing_bestseller = bestseller.filter(rating__gt=4) -> DB not touched yet so good for performance

	• print(bestseller) -> Now Django touches the DB and gets the Data

	• print(amaizing_bestseller) -> Django uses cahche data from previous query and does not touches the DB
	

--------------------------------------------------------------------------
• NOTE: Structure your query, and cache your query
--------------------------------------------------------------------------
	○ BAD USAGE:
		§ print( Book.objects.filter(rating__gt=3) ) -> 1st hit, bad
		§ print( Book.objects.filter(rating__gt=4) ) -> 2nd hit, bad
		§ good_books = Book.objects.filter(rating__gt=3) -> not hit, good
		§ print(good_books) -> 1 hit
		§ print(good_books.filter(rating__gt=4)) -> got from cache, not hit to DB