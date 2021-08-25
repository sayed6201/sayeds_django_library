from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# forms
from .forms import ProfileForm
# models
from .models import UserProfile

# Create your views here.
from django.views.generic.edit import CreateView

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


#=========================================================================
#View
    # Receiving form data and image in post() method and saving manually with model
#=========================================================================

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form":form
        })

    def post(self, request):
        # request.POST -> has only form data
        print(request.FILES["user_image"])

        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()

            # store_file(request.FILES["user_image"]) #manually saving in hardisk
            return HttpResponseRedirect("/profiles")
        else:
          return render(request, "profiles/create_profile.html",{
            "form":submitted_form
            })  

#=========================================================================
#CreateView
    # automatically saving data with model and redirecting to an url
    #handles both GET and POST automatically
#=========================================================================

class CreateProfileView(CreateView):
    template_name ="profiles/create_profile.html"
    model = UserProfile
    fields ="__all__" # render all the fields in the template
    success_url = "/profiles"