from django.contrib import admin
from django.urls import path
from .views import covidview

urlpatterns = [
    path('covid/',covidview),
    #path('admin/', admin.site.urls),
    

]
