from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from typing import Iterable, Optional



# Create your models here.

#======================================================
#book class extends/inherit models.Model class
#======================================================
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True,max_length=100)
    is_bestselling = models.BooleanField(default=False)

    #----------------------------------------------------
    #Slu is automatically filled when data is inserted
    # db_index=True, searching will be more efficient
    #----------------------------------------------------
    slug = models.SlugField(default="", null=False, db_index=True) #harry-potter-1


    #======================================================
    #Modifying the Built in save method
    #======================================================
    # def save(self, force_insert: bool, force_update: bool, using: Optional[str], update_fields: Optional[Iterable[str]]) -> None:

    #     #before saving a data, slug is created
    #     self.slug = slugify(self.title)

    #     return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    def save(self, *args, **kwargs):
        #before saving a data, slug is created
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    #======================================================
    # You can call the method from template
        # useage in template: <a href="{{ book.get_absolute_url }}"> </a>
    #======================================================
    def get_absolute_url(self):
        return reverse("detail-page", args={self.slug})
        

    #======================================================
    # you can define how output should show up in the terminal
    #======================================================
    def __str__(self):
        return f"{self.title} { self.rating }"
