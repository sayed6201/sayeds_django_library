

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.reviews),

    #=========================================================
    #vIEW AS A CLASS
    #=========================================================
    path('', views.ReiewView.as_view()),
    path('thank-you', views.thank_you),
]
