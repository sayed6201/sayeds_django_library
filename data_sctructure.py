
==========================================
Dictionary
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