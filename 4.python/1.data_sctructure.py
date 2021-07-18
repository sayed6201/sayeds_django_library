
==========================================
Dictionary code
==========================================
monthly_challenges_dictioinary = {
    "jan": "Eat no meat for entire month",
    "feb": "Walk 20 min",
    "mar": "Learn django"
}

#Dict -> List 
months = list(monthly_challenges_dictioinary.keys())

#length checking
if  month > len(monthly_challenges_dictioinary):
        return HttpResponseNotFound("Invalid month")

----------------------------
 #Slicing a list
----------------------------
latest_posts2 = all_posts[:-2] # All, except last 2 
latest_posts2 = all_posts[2:] # All, except first 2
latest_posts2 = all_posts[-2:] # only last 2  / all till 2nd data(reverses)
latest_posts2 = all_posts[:2] # only first 2  / all till 2nd data

----------------------------
 #Sorting a Dictionary
----------------------------
#helper function
def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    # all_posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
    
==========================================
List
==========================================
#Traverse
 for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

#length checking
len(months):