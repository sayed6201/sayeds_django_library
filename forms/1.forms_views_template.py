http://127.0.0.1:8000/?username=max




===============================================================
App/forms.py
===============================================================
from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name",
        max_length=100, 
        required=True, 
        error_messages={
        "required": "Your name must not be empty",
        "max_length": "Max length is 1000"
        
    }) #form label by default = User name




===============================================================
App/views.py
===============================================================
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.


def reviews(request): 
    
    form = ReviewForm()

    if request.method == 'POST':
        
    #     entered_username = request.POST['username'] #request.POST -> dictionary

    #     if entered_username == "" and len(entered_username) >= 100 :
    #         return render(request, "reviews/thankyou.html",{
    #             "has_error": True
    #         })

    #     print(entered_username)

    #     #Initiating Get request: reditecting to thank you page
    #     return HttpResponseRedirect("/thank-you")

        form = ReviewForm(request.POST)    

        if form.is_valid():
            print(form.cleaned_data())
            
    
    return render(request, "reviews/review.html",{
                "form": form
            })



def thank_you(request):
    return render(request, "reviews/thankyou.html")














===============================================================
App/templates/reviews.py
===============================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your review</title>
</head>
<body>

    <form action="/" method="POSt">
        # {% comment %} djago creates the token and validates it in the server,
        # the csrf token inficates the request is from actual server,
        # token changes every time the page is reloaded, 
        # server only accepts requests with valid token {% endcomment %}
        # {% csrf_token %} 

        

        # {% comment %} 
        #     <label for="username">Your name</label>
        #     <input id="username" name="username" type="text"> 
        # {% endcomment %}
        # {% comment %} {% if has_error %}
        #     <p>Invalid Form - Please enter your name</p>
        # {% endif %} {% endcomment %}


        # {% comment %} 
        #     forms.py will place label and field here
        #     no need of label and input tag 
        # {% endcomment %}
        {{form}}
    

        # {% comment %} does not send to server
        # <button type = "button" >Send</button> {% endcomment %}


        <button type = "submit" >submit</button>
    </form>

</body>
</html>
