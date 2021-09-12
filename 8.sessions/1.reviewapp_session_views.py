#=================================================================
#DetailView
    #review_detail page View Class
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


    #----------------------------------
    #Checking if the review is favorite
    #----------------------------------
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        #-----------------------------------------------------------------------------------
        #You can access the loaded objects and requests of this DetailView with "self" object
        loaded_review = self.object
        request = self.request

        #-----------------------------------------------------------------------------------
        #If session key is not defined it will show error, so use ->  " get[] "
            #favorite_id = request.session["favorite_review"] -> unsafe way, if null it will throw error
        favorite_id = request.session.get["favorite_review"] 

        #-----------------------------------------------------------------------------------
        #If favorite_id == loaded_review.id -> True
        #session value is always stored as string, so need to convert before comapring
        context["is_favorite"] = favorite_id == str(loaded_review.id)

        return context


#=================================================================
#Adding favourite data to session
#=================================================================
class AddFavoriteView(View):

    def post(self, request):
        review_id = request.POST["review_id"]

        fav_review = Review.objects.get(pk=review_id)

        #-----------------------------------------------------------------------------------
        #stroing data in session
            #You can not store objects in the sessions since it's not searilable
            #Serializable: django converts all var, dictionary, string into JSON
            #Data is always stored as string
                # request.session["favorite_review"] = fav_review -> you will get error if you store an object
        request.session["favorite_review"] = review_id

        return HttpResponseRedirect("/review/"+review_id)

