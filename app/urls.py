from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from app import views
urlpatterns = [
    path('category_list/',views.Category_list.as_view(),name='category_list'),
]