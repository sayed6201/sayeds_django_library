========================================================================
App/forms.py
========================================================================

from django import forms
from django.forms import fields
from .models import Review



#=================================================================
# Normal Form 
    # simple call -> {{form}} in template
    # NO need to create <input> fields in html
#=================================================================
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         max_length=100, 
#         required=True, 
#         error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Max length is 1000"
        
#     }) #form label by default = User name

#     review_text = forms.CharField(
#         label="Your Feedback",
#         widget=forms.Textarea,
#         max_length=200,
#     )

#     rating = forms.IntegerField(
#         label="Your rating",
#         min_value=1,
#         max_value=5
#     )





#=================================================================
# Model Form 
    # Links model attributes with form fields
    # Use ' class Meta: ' to customize the labels, erros,
#=================================================================
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields = "__all__" #creates form fields for all fields 

        # exclude = ['owner_comment'] #if you only want to exclude any fields from the template

        labels = {
            "user_name" : "Youe Name",
            "review_text" : "Youe Review",
            "rating" : "Your rating"
        }

        errors = {
            "user_name" : {
                "required" : "your name must not be empty ok",
                "max_length" : "Please enter a shorter name"
            },
        }