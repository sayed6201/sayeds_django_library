-----------------------------------
	#Traverse
-----------------------------------

 for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

        

-----------------------------------
	#Single Line forloop
-----------------------------------

#all_posts = [
# {}, {}
# ]
	idetifier_post = next( post for post in all_posts if post['slug'] == slug)