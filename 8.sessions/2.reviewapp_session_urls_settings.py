
#----------------------------------------------------
#Project > settings.py
	#Settings For Sessions.
#----------------------------------------------------
# SESSION_COOKIE_AGE = 120 #in seconds, by default it's 2 weeks






#=========================================================
#Project > settings.py
#=========================================================
from django.urls import path
from . import views

urlpatterns = [
    
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    
    #------------------------------------------------
    #<int:pk> -> Primary key
    #------------------------------------------------
    path('review/<int:pk>', views.SingleReviewView.as_view()),
]
