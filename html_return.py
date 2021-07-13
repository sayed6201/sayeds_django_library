
==========================================
returning HTML from view
==========================================
monthly_challenges_dictioinary = {
    "jan": "Eat no meat for entire month",
    "feb": "Walk 20 min",
    "mar": "Learn django"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges_dictioinary.keys())

    for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    # #static approach
    # response_data = """""
    # <ul>
    #     <li><a href="/challenges/jan">jan</a></li>
    # </ul>
    # """""

    return HttpResponse(response_data)