==============================================================================================================================
Terminal
Run the command to install Pillow
==============================================================================================================================

 RUN: python -m pip install Pillow



==============================================================================================================================
App>urls.py
==============================================================================================================================

from django.urls import path
from . import views



urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfileView.as_view()),

]




==============================================================================================================================
FILE UPLOAD SETUP:
    * FILE STOED DIR -> BASE_DIR / "uploads" / "images"
==============================================================================================================================
------------------------------------
* Step1: In Project > Settings.py add ->
------------------------------------

            MEDIA_ROOT = BASE_DIR / "uploads"

            #servered to the outside world
            MEDIA_URL = "/user-media/"


------------------------------------
* Step2: In App > models.py add ->
------------------------------------
image = models.ImageField(upload_to="images") 



------------------------------------
* Step3: In App > urls.py add ->
------------------------------------
from django.contrib import admin
from django.urls import path, include

#---------------------------------------------
#Fileupload setup imports
#---------------------------------------------
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" ,include("reviews.urls")),
    path("profiles/" ,include("profiles.urls"))

#You will need to give the files location and your url below 
        # to make it accessible in the browser
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

