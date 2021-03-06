==========================================
NOTE:
==========================================
* Extend -> 
        {% extends 'bootstrap_base.html' %} 

* Include and pass variable to include -> 
        {% include "challenges/includes/header.html" with active_page="index" %}

* Variable display -> 
        1. Accessing variable:
            {{ month|title }}

        2. Accessing Dictionary:
            <h3>{{ post.title }}</h3>        

* String Interpolation:
        1. <a href="/challenges/{{ month }}"></a>

        2. Concate string from variable:
            <img src="{% static "blog/images/"|add:post.image %}" alt="{{ post.title }}" />

        3. Mailto:
            <address>By  <a href="mailto:{{post.author.email}}"> {{ post.author }} </a></address>

* Block declaration -> 
        {% block content %}
            # your code goes here in child templates
        {% endblock  %}

* Filter text modification:
        1. <h1> {{ month|title }} Challenge </h1>
        2. <h2> {{ post.content|linebreaks }} <h2>
        3. <div>Last updated on <time> {{ post.date|date:"d M y" }}</time></div>


* Conditional Tags: 
        {% if text is not None %}
            <h2 >{{ text }}</h2>
        {% else %}
            <h2 class="mx-5 my-5">There is no challenge for this month</h2>
        {% endif %}

*LOOP Tags: 
        1.For Loop with include: 
            # included template will have access to all the variables 
            {% for post in posts %}
                {% include "blog/includes/post.html" %}
            {% endfor %}

        2.For Loop:
            {% for month in month_list %}
                {% comment %} 
                <li><a href="/challenges/{{ month }}">{{ month|title }}</a></li> 
                {% endcomment %}
                <li><a href="{% url "month-challenge" month %}">{{ month|title }}</a></li>
            {% endfor %}


==========================================
project/templates/base.html
==========================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block page_title %} My challenges {% endblock  %}</title>

    {% load static %}
    <link rel="stylesheet" href="{% static "style.css" %}"></link>

    {% block css_files %}

    {% endblock  %}
    
</head>
<body>

    {% block content %}

    {% endblock  %}

</body>
</html>



==========================================
app/templates/challenges/index.html
* extends -> base.html
* includes -> challenges/includes/header.html
==========================================
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
    {% include "challenges/includes/header.html" with active_page="index" %}
    <div class="card text-left card mx-5">
      <div class="card-body">
        <p class="card-text">
            <ul>
            {% for month in month_list %}
                {% comment %} <li><a href="/challenges/{{ month }}">{{ month|title }}</a></li> {% endcomment %}
                <li><a href="{% url "month-challenge" month %}">{{ month|title }}</a></li>
            {% endfor %}
            </ul>
        </p>
      </div>
    </div>
{% endblock  %}




==========================================
app/templates/challenges/challenges.html
* extends -> base.html
* includes -> challenges/includes/header.html
==========================================
{% extends 'base.html' %}

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
    
