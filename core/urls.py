"""scene URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url(r'^add/$', views.add_movie_page, name='add_movie_page'),
	url(r'^scrape/image/(?P<title>.*)/$', views.scrape_for_image, name='scrape_for_image'),
	url(r'^scrape/year/(?P<title>.*)/$', views.scrape_for_year, name='scrape_for_year'),
	url(r'^add/processing/$', views.add_movie, name='add_movie'),
	url(r'^movies/(?P<rating>[0-9]+)/$', views.movies_by_rating, name='movies_by_rating'),
	url(r'^search/$', views.search, name='search'),
	url(r'^about/$', views.about_page, name='about_page'),
]
