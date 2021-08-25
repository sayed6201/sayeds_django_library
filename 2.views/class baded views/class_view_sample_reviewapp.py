from django import forms
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

#Import View class 
from django.views import View

#Import TemplateView class
from django.views.generic.base import TemplateView

#Import Listview, DetailView
from django.views.generic import ListView, DetailView

#Import FormView class
from django.views.generic.edit import FormView, CreateView

# Create your views here.

#=================================================================#=================================================================
#Note: 
    # View: Use if you want to excplicitly define GET and POST request code
            #Import: from django.views import View

    # TemplateView, ListView, DetailView: 
                                # Use if you just want to pass data from GET Request
                                # No post request is supported
                                # Import: from django.views.generic.base import TemplateView
                                # Import: from django.views.generic import ListView, DetailView
    
    #FormView:
#=================================================================#=================================================================




========================================================================
App/views.py
========================================================================

#=================================================================
#View
    #View as a Class
    #You can define HTTP method , so no need to 
                            # -> if request.method == 'POST':
    #urls.py -> path('', views.ReiewView.as_view()),
#=================================================================
# class ReiewView(View):

#     #------------------------------------------------------
#     #GET Http method
#     #------------------------------------------------------
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html",{
#                     "form": form
#                 })


#     #------------------------------------------------------
#     #POST Http method
#     #------------------------------------------------------
#     def post(self, request):
#         form = ReviewForm(request.POST)    

#         if form.is_valid():
#             #------------------------------------------------------
#             #if you are using normal form, 
#             #------------------------------------------------------
#             # review  = Review(
#             #     user_name = form.cleaned_data["user_name"],
#             #     review_text = form.cleaned_data["review_text"],
#             #     rating = form.cleaned_data["rating"],
#             # )
#             # review.save()

#             #------------------------------------------------------
#             #if you are using model form, you can skip init model object
#             #------------------------------------------------------
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html",{
#                     "form": form
#                 })





#=================================================================
#FormView
    #loads from template without writing GET method
    #You can Validate form automatically
    #You can access form data and save in :  def form_valid(self, form)
#=================================================================
# class ReiewView(FormView):

#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)




#=================================================================
#CreateView
    #Advanced Version of FormView, use of you want to save data
    #loads from template without writing GET method
    #You can Validate form automatically
    #Saves data to model automatically

#UpdateView: You can Prepopulate form and update 
#DeleteView: You can delete the data
#=================================================================
class ReiewView(CreateView):
    model = Review
    form_class = ReviewForm
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"



#=================================================================
# TempleateView
    #ThankYou page TempleateView Class
    #You will write less code
    #You don't have GET, POST method
    #You can pass params with predifine methods
    #from django.views.generic.base import TemplateView
#=================================================================
class ThankYouView(TemplateView):
    #-----------------------------------------------------------
    #You don't have GET method in TemplateView
    #-----------------------------------------------------------
        # def get(self, request):
        #     return render(request, "reviews/thankyou.html")


    #-----------------------------------------------------------
    #whenever a Get request reaches it loads this view
    #-----------------------------------------------------------
    template_name = "reviews/thankyou.html"

    #-----------------------------------------------------------
    #Passing param using context to template
    #-----------------------------------------------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works"
        return context



#=================================================================
#TemplateView vs ListView
    #Display list with TemplateView
    #review_list page TempleateView Class VS ListView View Class
#=================================================================
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     #-----------------------------------------------------------
#     #Passing param using context to template
#     #-----------------------------------------------------------
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context




#=================================================================
# ListView
    #review_list page ListView View Class
    #You will write less code
    #You don't have GET, POST method
    #You can pass params with predifine methods
    #Import from: from django.views.generic import ListView, DetailView
#=================================================================
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"

    #All Rreview data as list
    model = Review

    #by default list name is -> object_list
        #You can change the name with -> context_object_name
    context_object_name = "reviews"

    #-----------------------------------------------------------
    #get_queryset(): Filter the list and return data
        #Optional Don't need to call if you don't intend to filter
    #-----------------------------------------------------------
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data



#=================================================================
#TemplateView
    #review_detail page Templeate View Class
#=================================================================
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     #-----------------------------------------------------------
#     #Passing param using context to template
#         #GET Request param can be accessed from: kwargs
#             #review/id -> kwargs['id']
#     #-----------------------------------------------------------
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context


#=================================================================
#DetailView
    #review_detail page Templeate View Class
    #Url: 'review/<int:pk>' 
                #-> by default DetailView passes data with pk to the template
                #You don't need to search by pk
    ##Import from: from django.views.generic import ListView, DetailView
#=================================================================
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    #-----------------------------------------------------------
    #You can Pass param using context to template if needed
    #-----------------------------------------------------------
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Manual Works below
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#=================================================================
#View as methods
    #You can code view as methods
    # You will have to manually check if the request is POST or GET
    # You will have to render template manually
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