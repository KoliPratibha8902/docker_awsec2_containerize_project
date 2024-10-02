# devops/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple home view to handle the root URL
def home_view(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('', home_view, name='home'),  # Root URL route
    path('demo/', include('demo.urls')),  # Include URLs for the 'demo' app
    path('admin/', admin.site.urls),  # Admin URL
]




# """devops URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('demo/', include('demo.urls')),
#     path('admin/', admin.site.urls),
# ]
