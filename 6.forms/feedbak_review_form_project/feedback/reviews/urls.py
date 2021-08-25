

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.reviews),

    #=========================================================
    #vIEW AS A CLASS
    #=========================================================
    path('', views.ReiewView.as_view()),
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewsListView.as_view()),

    #------------------------------------------------
    #<int:pk> -> Primary key
    #------------------------------------------------
    path('review/<int:pk>', views.SingleReviewView.as_view()),
]
