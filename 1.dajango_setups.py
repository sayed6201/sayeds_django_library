===============================================================
App Setup:
===============================================================

RUN: python manage.py startapp appname -> to create APP

--------------
app/urls.py
--------------
	from django.urls import path
	from . import views # . -> from same folder
	urlpatterns = [
	    path("jan", views.jan), #if the url is "January" then execute views.index
	    path("feb", views.feb)
	]

--------------------
project/urls.py
---------------------
	from django.contrib import admin
	from django.urls import path, include
	urlpatterns = [
    
	    path('admin/', admin.site.urls),

	    #including the challenges app urls to project
	    path("challenges/", include("challenges.urls"))
    ]


===============================================================
Template Setup:
---------------
* Django can auto detect 'Template' folder in app level, 
	* if 'APP_DIRS': True and 
	* App name is in INSTALLED_APPS
* Django can not auto detect 'Template' folder in project level, 
	* so add them in TEMPLATES -> dirs
===============================================================

--------------
* Step1: 
--------------

Create-> template/appname/yourhtmlfile.html 
example: template/challenges/challenges.html 


-------------------
* Step2: Register app in -> project/setting.py
------------------
# Application definition
INSTALLED_APPS = [
    #Registering Aware of our app, now django can find tamplate
    'challenges',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


---------------------------------------------------------------
* Step3: Register template -> project/setting.py
---------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  #base template

            #you can add tamplates here, if it's a global (outside of app)
            # BASE_DIR / "challenges" / "tamplates"

        ],
        'APP_DIRS': True, #will look for tamplate in app folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



==========================================================
CSS Setup:
---------------
* Django can auto detect 'static' folder in app level, 
	
* Django can not auto detect 'static' folder in project level, 
	* so add it in -> STATICFILES_DIRS
==========================================================

#Created by me to introduce global static folder to Django
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
