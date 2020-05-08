from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('',views.articles,name = "articles"),
    
]
