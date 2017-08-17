from django.shortcuts import render, redirect
from .models import Movie

from lxml import etree
import urllib2

# Create your views here.

def home_page(request):
	movies = Movie.objects.all()
	return render(request, 'home_page.html', {'movies':movies})

def scrape_for_image(title):
	title = title.replace(" ", "_")
	title = title.replace("'", "")
	title = title.replace(":", "")
	title = title.replace("/", " ")
	title = title.replace(".", "")
	title = title.lower()

	url = "https://www.rottentomatoes.com/m/" + title

	req = urllib2.Request(url, headers={'user-Agent' : 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'})
	page_html = urllib2.urlopen(req).read()

	html_dom = etree.HTML(page_html)

	poster = html_dom.xpath('//div[@id="movie-image-section"]//img/@src')[0]

	return poster

def scrape_for_year(title):

	title = title.replace(" ", "_")
	title = title.replace("'", "")

	url = "https://www.rottentomatoes.com/m/" + title

	req = urllib2.Request(url, headers={'user-Agent' : 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'})
	page_html = urllib2.urlopen(req).read()

	html_dom = etree.HTML(page_html)

	year = html_dom.xpath('//span[@class="h3 year"]/text()')[0]

	year = year.replace(" ", "")
	year = year.replace("(", "")
	year = year.replace(")", "")
	year = int(year)

	return year


def add_movie_page(request):
	return render(request, 'add_movie_page.html')

def add_movie(request):
	title = request.POST.get("title")
	comments = request.POST.get("comments")
	rating = request.POST.get("rating")

	year = scrape_for_year(title)
	image = scrape_for_image(title)

	movie = Movie.objects.create(title=title, comments=comments, year=year, image=image, rating=rating)
	return redirect(home_page)

def movies_by_rating(request, rating):
	movies = Movie.objects.filter(rating=rating)
	return render(request, 'movies_by_rating.html', {'movies':movies, 'rating':rating})

def search(request):
	term = request.POST.get("term")
	movies = Movie.objects.all()

	results = []
	for movie in movies:
		if term in movie.title:
			results.append(movie)
		elif term in movie.comments:
			results.append(movie)
		elif term in str(movie.year):
			results.append(movie)

	return render(request, 'search_results.html', {'term':term, 'results':results})

def about_page(request):
	return render(request, 'about_page.html')




