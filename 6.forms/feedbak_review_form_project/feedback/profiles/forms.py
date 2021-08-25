from django import forms
    
class ProfileForm(forms.Form):
    #For all types of files
    # user_image = forms.FileField()

    #For all images
    user_image = forms.ImageField()