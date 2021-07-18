===============================================================
App/urls.py
===============================================================


from django.urls import path
from . import views # . -> from same folder

urlpatterns = [
    #============================================
    #if the url is "January" then execute views.index
    #============================================
    # path("jan", views.jan), 
    # path("feb", views.feb),

    #============================================
    #dynamic placeholder, month could be jan, feb
            ##dynamic placeholder type-> str, int
    #============================================
    path("<int:month>", views.monthly_challenge_bynum), 
    #path("<str:month>", views.monthly_challenge), 

    #============================================
    #named urls
        #name = name of the url, 
        #now you don't have to write challenges/month in your code
        #in future if challnges is changes in the project urls then it won't be a problem
        #using named url in views.py -> reverse() will auto generate link to the url
            #redirect_path = reverse("month-challenge", args=[redirect_month]) # -> "/challenges/jan"
        #using named url in template -> <a href="{% url "month-challenge" month %}">{{ month|title }}</a>
    #============================================
    path("<str:month>", views.monthly_challenge, name="month-challenge"), 

    #============================================
    #Creating a dynamic challnege app index page
    #============================================
    path("", views.index, name="index") # /challenges/



    #============================================
    #Slug
    #============================================
    path("post/<slug:slug>", views.post_detail, name="post-detail-page") #/posts/my-first-post, slug fotmate 
]




===============================================================
Project/urls.py
===============================================================

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"))
]