from django.contrib import admin

from .models import Authors, Book, Address

# Register your models here.


#==========================================================
# BookAdmin -> configures Admin UI settings
#==========================================================
class BookAdmin(admin.ModelAdmin):
    
    #----------------------------------------------------
    #You can only view the fields in the Admin UI
    #----------------------------------------------------
    # readonly_fields = ("slug",)


    #----------------------------------------------------
    #filled automatically with slug formate when you type
        # you don't need the save() in models.py
    #----------------------------------------------------
    prepopulated_fields = {
        "slug": ("title",)
    }


    #----------------------------------------------------
    #you can filter data in the admin panel by these fields
    #----------------------------------------------------
    list_filter = ["author", "rating"]


    #----------------------------------------------------
    #title and author will show in the admin panel
    #----------------------------------------------------
    list_display = ["title", "author",]


#==========================================================
# BookAdmin -> configures Admin UI settings
#==========================================================
class AuthorsAdmin(admin.ModelAdmin):


    #----------------------------------------------------
    #title and author will show in the admin panel
    #----------------------------------------------------
    list_display = ["first_name", "last_name",]




#==========================================================
# Register the models and realted admin setting here
#==========================================================
admin.site.register(Book, BookAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Address)
