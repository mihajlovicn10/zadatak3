"""zadatak3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book import views as book_views
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView

import book


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path("book-list/", book_views.book_list),
    path("book-add/", book_views.book_add), 
    path("book-delete/<str:pk>/", book_views.book_delete),
    path("book-update/<str:pk>/", book_views.book_update),
    path("book_list_ui/",book_views.book_list_ui), 
    path('book_delete_ui/<str:pk>/',book_views.book_delete_ui), 
    path('make/',book_views.make_api_key),
    path('generate/',book_views.generate)

]
