========================================================================
* Sending data from Views to the template
* app/views.py
* send var using -> 
            render(request,"challenges/challenge.html", {
                "text" : challenges_text,
                "month" : month})
========================================================================

from django import urls
import challenges
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



monthly_challenges_dictioinary = {
    "jan": "Eat no meat for entire month",
    "feb": "Walk 20 min",
    "mar": "Learn django",
    "april": None,
}

def index(request):
    list_items = ""
    months = list(monthly_challenges_dictioinary.keys())

    #--------------------------
    # Creating <li> with loop 
    #--------------------------
    # for month in months:
    #     capitalized_months = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    #--------------------------
    # #Multi line string
    #--------------------------
    # response_data = """""
    # <ul>
    #     <li><a href="/challenges/jan">jan</a></li>
    # </ul>
    # """""

    return render(request, "challenges/index.html", {
        "month_list" : months
    })

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges_dictioinary[month]

        #sending html, f enables strong interpolation and can inject var

        # response_data = f"<h1>{challenges_text}</h1>"

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        #shortcut of -> render_to_string + HttpResponse
        return render(request,"challenges/challenge.html", {
            "text" : challenges_text,
            "month" : month
        })

    except:
        response_data = render_to_string("404.html")
        # return HttpResponseNotFound("<h1>Not supported</h1>")
        #render() -> can not be used becoz it shows success page, it showa 200 not 404
        # return HttpResponseNotFound(response_data)
        raise Http404() #it will search for 404 page in the templates


========================================================================
* Accessing data from Views in the template
* to access the passed variable -> {{ month|title }}
* string interpolation -> "/challenges/{{ month }}"
========================================================================

-------------------------------------------------------
-------------------------------------------------------
Challenges Page
-------------------------------------------------------
-------------------------------------------------------

{% extends 'bootstrap_base.html' %}

{% block page_title %}
    Monthly Challenges
{% endblock  %}

{% block content %}
    
    {% include "challenges/includes/header.html" with active_page="challenge" %}

    <div class="mx-5">
        <h1>{{ month|title }}'s Challenge</h1>
        {% if text is not None %}
            <h2 >{{ text }}</h2>
        {% else %}
            <h2 class="mx-5 my-5">There is no challenge for this month</h2>
        {% endif %}
    </div>
{% endblock  %}
    


-------------------------------------------------------
-------------------------------------------------------
* page: Index.py
* 
-------------------------------------------------------
-------------------------------------------------------

{% extends 'bootstrap_base.html' %} 

{% comment %} 
{% extends '../../../templates/base.html' %} 
add base dir in sttings.py
{% endcomment %}

{% load static %}

{% block css_files %}
    {% comment %} 
    <link rel="stylesheet" href="{% static "challenges/challenges.css" %}"> </link> 
    {% endcomment %}
{% endblock  %}

{% block page_title %}
    Monthly Challenges
{% endblock  %}

{% block content %}

            <ul>
            {% for month in month_list %}
                {% comment %} <li><a href="/challenges/{{ month }}">{{ month|title }}</a></li> {% endcomment %}
                <li><a href="{% url "month-challenge" month %}">{{ month|title }}</a></li>
            {% endfor %}
            </ul>

{% endblock  %}
