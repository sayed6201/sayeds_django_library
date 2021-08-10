from django import forms
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
# Create your views here.


#=================================================================
#View as a Class
from django.views import View
    #You can define HTTP method , so no need to 
                            # -> if request.method == 'POST':
    #urls.py -> path('', views.ReiewView.as_view()),
#=================================================================
class ReiewView(View):

    #------------------------------------------------------
    #GET Http method
    #------------------------------------------------------
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html",{
                    "form": form
                })


    #------------------------------------------------------
    #POST Http method
    #------------------------------------------------------
    def post(self, request):
        form = ReviewForm(request.POST)    

        if form.is_valid():
            #------------------------------------------------------
            #if you are using normal form, 
            #------------------------------------------------------
            # review  = Review(
            #     user_name = form.cleaned_data["user_name"],
            #     review_text = form.cleaned_data["review_text"],
            #     rating = form.cleaned_data["rating"],
            # )
            # review.save()

            #------------------------------------------------------
            #if you are using model form, you can skip init model object
            #------------------------------------------------------
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html",{
                    "form": form
                })






#=================================================================
#View as methods
#=================================================================
def reviews(request): 

    if request.method == 'POST':

        #-------------------------------------------------------------------------------------
        # Manual form validation
        #-------------------------------------------------------------------------------------
        #     entered_username = request.POST['username'] #request.POST -> dictionary

        #     if entered_username == "" and len(entered_username) >= 100 :
        #         return render(request, "reviews/thankyou.html",{
        #             "has_error": True
        #         })

        #     print(entered_username)

            #Initiating Get request: reditecting to thank you page
            #return HttpResponseRedirect("/thank-you")

        #-------------------------------------------------------------------------------------
        # Auton form validation using forms.py
        #-------------------------------------------------------------------------------------
        form = ReviewForm(request.POST)    

            #-------------------------------------------------------------------------------------
            #You can Populate a form by passing 'instance'
            #-------------------------------------------------------------------------------------
            # existing_data = Review.objects.get(pk=1)
            # form = ReviewForm(request.POST, instance=existing_data)    

        #Auto validation
        if form.is_valid():
            # print(form.cleaned_data)
            # review  = Review(
            #     user_name = form.cleaned_data["user_name"],
            #     review_text = form.cleaned_data["review_text"],
            #     rating = form.cleaned_data["rating"],
            # )
            # review.save()

            #-------------------------------------------------------------------------------------
            #if you are using model form, you can skip init model object -> review  = Review(..)
            #-------------------------------------------------------------------------------------
            form.save()
            #redirecting to thank you page -> GET request
            return HttpResponseRedirect("/thank-you")

    # Exectes when GET requst or page is first loaded
    else:
        #Init form so that you can display it in the tempalte
        form = ReviewForm()
            
    
    return render(request, "reviews/review.html",{
                "form": form
            })


def thank_you(request):
    return render(request, "reviews/thankyou.html")