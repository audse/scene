from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=140)
	image = models.CharField(max_length=1024, blank=True, null=True)
	year = models.IntegerField(blank=True, null=True)

	rating = models.IntegerField(default=3)
	comments = models.TextField()

	def __str__(self):
		return self.title + ": " + str(self.rating) + "/5"

