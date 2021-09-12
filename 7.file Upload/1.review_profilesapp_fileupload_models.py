from django.db import models

# Create your models here.

class UserProfile(models.Model):

    #-------------------------------------------------------------------------
    # FileField
        #The file will not be stored in the DB, only the path will be sotred 
            # for this define-> upload_to="images"
        #Files will be stored in Harddrive
        #In setting do -> MEDIA_ROOT = BASE_DIR / "uploads" / "Images"
            # Now the image will be stored in -> BASE_DIR / "uploads" / "Images"
    #-------------------------------------------------------------------------
    # image = models.FileField(upload_to="images")



    #-------------------------------------------------------------------------
    #ImageField
        #Only accepts images
        #You will need to install: python -m pip install Pillow
        #The file will not be stored in the DB, only the path will be sotred 
            # for this define-> upload_to="images"
        #In peoject > setting.py do -> MEDIA_ROOT = BASE_DIR / "uploads" / "Images"
            # Now the image will be stored in -> BASE_DIR / "uploads" / "Images"

    #Displaying image:
        #Use to access the url in browser -> profile.image.url
        #Use to access the path in browser -? profile.image.path
        #Image is not accessible without a setting change since django hides all folder in browser
            #STEP1: In Project>setting.py Add-> MEDIA_ROOT = BASE_DIR / "uploads"
                                            # MEDIA_URL = "/user-media/"
            #STEP2: In project>urls.py add ->
                                #Imports:
                                    # from django.conf.urls.static import static
                                    # from django.conf import settings

                                    # urlpatterns = [
                                    #     path('admin/', admin.site.urls),
                                    #     path("" ,include("reviews.urls")),
                                    #     path("profiles/" ,include("profiles.urls"))

                                    # #You will need to give the files location and your url below 
                                    #         # to make it accessible in the browser
                                    # ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #-------------------------------------------------------------------------
    image = models.ImageField(upload_to="images") 
