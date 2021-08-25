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
        #In setting do -> MEDIA_ROOT = BASE_DIR / "uploads" / "Images"
            # Now the image will be stored in -> BASE_DIR / "uploads" / "Images"
    #-------------------------------------------------------------------------
    image = models.ImageField(upload_to="images") 